<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>


<html>
<head>
<title>무신사 남성 랭킹</title>
<link rel="stylesheet" type="text/css" href="css/styles.css">

<script type="text/javascript">
	function showOuter(imageUrl, image) {
		
		if (image.classList.contains('selected')) {
			image.classList.remove('selected');
		}
		else {
			image.classList.add('selected');
			document.getElementById("preview-outer").src = imageUrl;
		}
	}
	function showTop(imageUrl, image) {

		if (image.classList.contains('selected')) {
			image.classList.remove('selected');
		}
		else {
			image.classList.add('selected');	
			document.getElementById("preview-top").src = imageUrl;
		}
	}
	function showPants(imageUrl, image) {

		if (image.classList.contains('selected')) {
			image.classList.remove('selected');
		}
		else {
			image.classList.add('selected');
			document.getElementById("preview-pants").src = imageUrl;
		}
	}
</script>
</head>
<body>


	<div style="width: 100%; height: 8vh;  font-weight: bold; color: white; background-color: black; ">
		<h3 style="display: inline-block; margin:0px; font-size: 25px; line-height: 8vh;">&nbsp;MUSINSA RANKING FOR MEN</h3>
		<p style="display: inline-block; margin:0px; float:right; line-height: 8vh;">목록 업데이트 :&nbsp;<fmt:formatDate value="${outerList[0].updatedate}" pattern="yyyy년 MM월 dd일 HH시mm분"/>&nbsp;&nbsp;</p>
	</div>




	<div class="image-container">
		<div style="display: flex;">
			<img class="preview-img" id="preview-outer" src="images/black.jpg"
				alt="Image 1">
			<div class="name">아우터</div>
		</div>
		<div style="display: flex;">
			<img class="preview-img" id="preview-top" src="images/black.jpg"
				alt="Image 2">
			<div class="name">상의</div>
		</div>
		<div style="display: flex;">
			<img class="preview-img" id="preview-pants" src="images/black.jpg"
				alt="Image 3">
			<div class="name">바지</div>
		</div>
	</div>
	<div class="musinsalist">
		<div class="container">
			<c:forEach var="outer" items="${outerList}">
				<div class="card-wrapper">
					<div class="card">
						<div id=img onclick="showOuter('${outer.imglink}', this)">
							<img src="${outer.imglink}" alt="images/black.jpg">
							<h4 class=img_id>${outer.outer_id}위</h4>
						</div>
						<div class="card-text">
							<a href="${outer.link}" target="_blank" class="title">${outer.title}</a>
						</div>
						<p class="brand">${outer.brand}</p>
						<div class="card-desc">
							<p class="price">${outer.price}</p>
							<p class="star">★${outer.star}(${outer.starnum})</p>
						</div>

					</div>
				</div>
			</c:forEach>
		</div>

		<div class="container">
			<c:forEach var="top" items="${topList}">
				<div class="card-wrapper">
					<div class="card">
						<div id=img onclick="showTop('${top.imglink}', this)">
							<img src="${top.imglink}" alt="images/black.jpg">
							<h4 class=img_id>${top.top_id}위</h4>
						</div>
						<div class="card-text">
							<a href="${top.link}" target="_blank" class="title">${top.title}</a>
						</div>
						<p class="brand">${top.brand}</p>
						<div class="card-desc">
							<p class="price">${top.price}</p>
							<p class="star">★${top.star}(${top.starnum})</p>
						</div>

					</div>
				</div>
			</c:forEach>
		</div>

		<div class="container">
			<c:forEach var="pants" items="${pantsList}">
				<div class="card-wrapper">
					<div class="card">
						<div id=img onclick="showPants('${pants.imglink}', this)">
							<img src="${pants.imglink}" alt="images/black.jpg">
							<h4 class=img_id>${pants.pants_id}위</h4>
						</div>
						<div class="card-text">
							<a href="${pants.link}" target="_blank" class="title">${pants.title}</a>
						</div>
						<p class="brand">${pants.brand}</p>
						<div class="card-desc">
							<p class="price">${pants.price}</p>
							<p class="star">★${pants.star}(${pants.starnum})</p>
						</div>

					</div>
				</div>
			</c:forEach>
		</div>


	</div>


</body>
</html>