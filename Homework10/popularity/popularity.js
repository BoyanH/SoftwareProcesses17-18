const json2csv = require('json2csv');
const countries = require('country-list')();
const fs = require('fs');
const googleTrends = require('google-trends-api');

const keyword = 'cataclysm dda';
const startTime = new Date(2017, 0, 1);
const endTime = new Date(2018, 0, 6);

const countryCodes = countries.getCodes();
// for debugging purposes, easy to test by comparing results with the ones of the web interface
// const countryCodes = ['DE', 'US', 'AU'];
const fields = ['date', 'value'];
let globalPopularity = [];


googleTrends.interestOverTime({keyword: keyword, startTime: startTime, endTime: endTime})
    .then((results) => {
        const tlData = JSON.parse(results).default.timelineData;
        tlData.forEach((result) => {
            globalPopularity.push({
                date: new Date(result.formattedAxisTime).toLocaleDateString(),
                value: result.value[0]
            });
        });

        const csv = json2csv({data: globalPopularity, fields: fields});
        fs.writeFile('global_popularity.csv', csv, (err) => {
            if (err) throw err;
            console.log('global popularity saved');
        });
    })
    .catch(err => console.log(err));

const resultsPerLocale = {};
const overPopularityCSVNames = ['overTen.csv', 'overTwenty.csv', 'overFifty.csv', 'overHundred.csv'];
const overPopularity = [{}, {}, {}, {}];
const overPopularityValues = [10, 20, 50, 100];

queryLocales(() => {
   // find all the available dates for which we have info
   const dates = [];
   countryCodes.forEach((code) => {
        const perLocale = resultsPerLocale[code];

        if (!perLocale || !perLocale.default) {
            return;
        }

        const tlData = perLocale.default.timelineData;
        tlData.forEach((tl) => {
            const dateStr = new Date(tl.formattedAxisTime).toLocaleDateString();
            if (dates.indexOf(dateStr) === -1) {
                dates.push(dateStr);
            }
        });
   });

   // initialize number of countries with popularity over n for each date
   // initial value is 0
   dates.forEach((date) => {
      overPopularity.forEach((value, idx) => {
          overPopularity[idx][date] = 0;
      })
   });

   // fill popularity info
   countryCodes.forEach((code) => {
        const perLocale = resultsPerLocale[code];

        if (!perLocale || !perLocale.default) {
            return;
        }

        const tlData = perLocale.default.timelineData;
        tlData.forEach((tl) => {
            const dateStr = new Date(tl.formattedAxisTime).toLocaleDateString();

            overPopularityValues.forEach((value, idx) => {
                if (tl.value >= value) {
                    overPopularity[idx][dateStr] += 1;
                }
            });

        });
   });

   // format data for csv saving and save it
   overPopularityCSVNames.forEach((name, idx) => {
      const popularity = overPopularity[idx];
      const inCSVForm = [];

      dates.forEach((date) => {
          inCSVForm.push({
              date: date,
              value: popularity[date]
          })
      });

      const csv = json2csv({data: inCSVForm, fields: fields});
        fs.writeFile(name, csv, (err) => {
            if (err) throw err;
            console.log(`${name} saved!`);
        });
   });
});


function queryLocales(callback, idx=0) {
    console.log(idx + 1, 'out of', countryCodes.length);
    if (idx === countryCodes.length) {
        callback();
    } else {
        const next = () => queryPopularityInLocale(countryCodes[idx], (res) => {
           resultsPerLocale[countryCodes[idx]] = res;
           queryLocales(callback, idx + 1);
        });

        // need some timeout between requests, otherwise google isn't really happy with what we are doing
        setTimeout(next, 200);
    }
}

function queryPopularityInLocale(code, callback) {
    googleTrends.interestOverTime({
        keyword: keyword,
        startTime: startTime,
        endTime: endTime,
        geo: code,
    })
        .then((res) => {
            callback(JSON.parse(res));
        })
        .catch((err) => {
            console.log(err);
            callback({});
        });
}