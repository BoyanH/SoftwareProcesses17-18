# Gather popularity information in CSV format from google trends

## Output

Outputs a global popularity file, as well as files with the amount of countries per date with popularity
more or equal to 10%, 20%, 50% and 100%

## Usefulness

The data should allow us to tell how the popularity grows or shrinks after some code changes and feature
development. The global popularity is self explaining.


The number of countries with popularity more than n% should be able to tell us a couple of things.

1. In how many countries the game is being used (over 10%, only countries with data (where game is used at all)
and a sufficient interest in the game (not a huge drop in popularity) will be counted)
1. Data with higher popularity percentages should tell us in how many countries there is a trend to play this game
  and how big it is.

*Important!:* we cannot do any comparison between countries with this data, as it only uses percentages, which are
normalized using the total usage in a given country. This is however possible to do with google trends, though we
don't really find it useful, as bigger countries are expected to have a bigger share of the total usage. This isn't
really interesting in our case, the relative percentages are much more helpful.