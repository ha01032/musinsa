package com.example.musinsa.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.example.musinsa.service.ScrollService;

import lombok.RequiredArgsConstructor;




@Controller
@RequiredArgsConstructor
public class ScrollController {
	
	@Autowired private final ScrollService scrollService;

	@GetMapping("/")
	public ModelAndView getmusinsalist() {
		ModelAndView mav = new ModelAndView();
		
		scrollService.getmusinsalist(mav);
		
		return mav;
	}

}
