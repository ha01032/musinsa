package com.example.musinsa.model;

import java.util.Date;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Pants {
	
	private int pants_id;
	private String title;
	private String link;
	private String price;
	private String brand;
	private String star;
	private String starnum;
	private String imglink;
	private Date updatedate;
}

