package com.javacode.data.model;

public class Student {

	String name;
	String exam;
	String date;
	String reden;
	int rollNumber;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getExam() {
		return exam;
	}
	public void setExam(String exam) {
		this.exam = exam;
	}
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}
	public String getReden() {
		return reden;
	}
	public void setReden(String reden) {
		this.reden = reden;
	}
	public int getRollNumber() {
		return rollNumber;
	}
	public void setRollNumber(int rollNumber) {
		this.rollNumber = rollNumber;
	}
	
	@Override
	public String toString(){
		return name+" "+exam+" op "+ date+"met reden: "+ reden;
	}
}
