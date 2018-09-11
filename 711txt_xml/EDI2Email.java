package com.danonewave.editesting.target2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class EDI2Email {
	private static final String RECORD_DELIMITER = "~";
	private static final String FIELD_DELIMITER = "*";

	public void main(String[] args) throws Exception {
		File ediFile = new File(args[0]);
		File emailFile = new File(args[1]);

		FileReader ediFileReader = new FileReader(ediFile);
		FileReader emailFileReader = new FileReader(emailFile);
		BufferedReader ediBufferedReader = new BufferedReader(ediFileReader);
		BufferedReader emailBufferedReader = new BufferedReader(emailFileReader);

		String ediLine;
		String emailLine;
		while ((ediLine = ediBufferedReader.readLine()) != null) {
			String[] ediFields = ediLine.split(FIELD_DELIMITER);
			String ediSegment = ediFields[0];
			switch (ediSegment) {
			case "ISA":
			case "GS":
			case "ST":
			case "SE":
			case "GE":
			case "IEA":
			case "":
				// ignore
				break;
			default:
				for (int i = 1; i < ediFields.length; i++) {
					String ediField = (i == ediFields.length - 1) ? ediFields[i].replace(RECORD_DELIMITER, "")
							: ediFields[i];
					String ediFieldPosition = getPosition(i);
					while ((emailLine = emailBufferedReader.readLine()) != null) {
						if (emailLine.length() > 50 && emailLine.charAt(50) == '='){
							String[] emailSegment = emailLine.substring(0,15).trim().split("_");
							if (emailSegment.length == 3){
								
							}else{
								
							}
						}
					}
				}
			}
		}
		ediFileReader.close();
		emailFileReader.close();
	}

	private static String getPosition(int index) {
		if (index < 10) {
			return "0" + index;
		} else {
			return String.valueOf(index);
		}
	}
}
