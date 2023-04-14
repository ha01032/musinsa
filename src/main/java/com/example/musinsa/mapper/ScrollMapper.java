package com.example.musinsa.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.example.musinsa.model.Outer;
import com.example.musinsa.model.Pants;
import com.example.musinsa.model.Top;


@Mapper
public interface ScrollMapper {
	
	
	List<Top> topList();
	List<Pants> pantsList();
	List<Outer> outerList();
	
	
	
}
