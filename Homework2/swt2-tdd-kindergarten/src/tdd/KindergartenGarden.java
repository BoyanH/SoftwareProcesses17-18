package tdd;

import java.util.Arrays;
import java.util.List;
import java.util.NoSuchElementException;

public class KindergartenGarden {

	private String plants;
	private String[] studentNames = {};

	public static Plant getPlant(char plantLetter) {
		switch(plantLetter) {
			case 'V': return Plant.VIOLETS;
			case 'C': return Plant.CLOVER;
			case 'R': return Plant.RADISHES;
			case 'G': return Plant.GRASS;
			default: throw new IllegalArgumentException("No such plant!");
		}
	}

	public KindergartenGarden(String plants) {
		this.plants = plants;
                this.studentNames = new String[] {"Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"};
	}

	public KindergartenGarden(String plants, String[] names) {
		this.plants = plants;
		this.studentNames = names;
		Arrays.sort(this.studentNames);
	}

	public int getOffsetForStudent(String name) {
		int offset = Arrays.asList(this.studentNames).indexOf(name)*2;
                
                if (offset < 0){
                    throw new NoSuchElementException("Unknown student");
                }
                
                return offset;
	}

	public List<Plant> getPlantsOfStudent(String name) {
		String[] rows = this.plants.split("\n");
		int offset = getOffsetForStudent(name);

                
		return Arrays.asList(   getPlant(rows[0].charAt(offset)), 
                                        getPlant(rows[0].charAt(offset + 1)),
                                        getPlant(rows[1].charAt(offset)), 
                                        getPlant(rows[1].charAt(offset + 1)));
	}

}
