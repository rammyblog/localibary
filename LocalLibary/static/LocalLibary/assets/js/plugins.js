/*global $,window*/
$(function () {
    "use strict";
// Nice Scroll
    $("html").niceScroll();

// Click on Search Icon to show Search input
    $(".menu .menu-section .search").click(function () {
        $(".menu .menu-section .search, .menu .menu-section .search-bar").toggleClass("active");
        $(".menu .menu-section .search-bar input").focus();
    });

// Click on Cart Icon to show Cart SHOPPING CART
    $("#cart").on("click", function () {
        $(".shopping-cart").fadeToggle("fast");
    });

//Click on Menu Toggle to see Site pages
    $(".menu-toggle").on("click", function () {
        $(this).toggleClass("on");
        $(".menu-section").toggleClass("on");
        $("nav ul").toggleClass("hidden");
    });

// Show Color Option Div When Click On The Gear
    $(".gear-check").click(function () {
        $(".color-option").fadeToggle();
    });

// Change Theme Color On Click
    var colorLi = $(".color-option ul li");
    colorLi.eq(0).css("backgroundColor", "#3498db").end()

        .eq(1).css("backgroundColor", "#2ecc71").end()

        .eq(2).css("backgroundColor", "#1abc9c").end()

        .eq(3).css("backgroundColor", "#f1c40f").end()

        .eq(4).css("backgroundColor", "#f39c12").end()

        .eq(5).css("backgroundColor", "#e67e22").end()

        .eq(6).css("backgroundColor", "#e74c3c").end()

        .eq(7).css("backgroundColor", "#95a5a6").end()

        .eq(8).css("backgroundColor", "#9b59b6").end()

        .eq(9).css("backgroundColor", "#34495e").end()

        .eq(10).css("backgroundColor", "#A0522D").end()

        .eq(11).css("backgroundColor", "#FF69B4").end()

        .eq(12).css("backgroundColor", "#B8860B").end()

        .eq(13).css("backgroundColor", "#87CEFA").end()

        .eq(14).css("backgroundColor", "#000000");
    colorLi.click(function () {
        $("link[href*='theme']").attr("href", $(this).attr("data-value"));
    });

// Adjust Header Height
    var myHeader = $(".home-background"),
        mySlider = $(".home-background-head-text");
    myHeader.height($(window).height());
    mySlider.each(function () {
        $(this).css("paddingTop", ($(window).height() - $(".home-background-head-text").height()) / 2);
    });

//When your resize the window the Header will take the window"s width and height
    $(window).resize(function () {
        myHeader.height($(window).height());
        mySlider.each(function () {
            $(this).css("paddingTop", ($(window).height() - $(".home-background-head-text").height()) / 2);
        });
    });

// Click on fa-angle-down Button to Move Down to Section Three
    $(".fa-angle-down").click(function () {
        $("html, body").animate({
            scrollTop: $(".home-page-section-three").offset().top
        }, 1000);
    });
    
//Authors Slider
    // Activate Carousel
    $("#myCarousel").carousel({interval: 6000, pause: "hover"});
    // Enable Carousel Indicators
    $(".item1").click(function () {
        $("#myCarousel").carousel(0);
    });
    $(".item2").click(function () {
        $("#myCarousel").carousel(1);
    });
    $(".item3").click(function () {
        $("#myCarousel").carousel(2);
    });
    $(".item4").click(function () {
        $("#myCarousel").carousel(3);
    });
    // Enable Carousel Controls
    $(".left").click(function () {
        $("#myCarousel").carousel("prev");
    });
    $(".right").click(function () {
        $("#myCarousel").carousel("next");
    });
//Click on Show More Button to See All Paragraphs
    var firstPara = $(".tab-pane p").eq(2),
        secondPara = $(".tab-pane p").eq(3),
        thirdPara = $(".tab-pane p").eq(4);
    firstPara.hide();
    secondPara.hide();
    thirdPara.hide();
    $("a.more").on("click", function (event) {
        event.preventDefault();
        if (firstPara.is(":hidden") && secondPara.is(":hidden") && thirdPara.is(":hidden")) {
            firstPara.slideDown("fast");
            secondPara.slideDown("fast");
            thirdPara.slideDown("fast");
            $(this).html("read less <i class='fa fa-angle-up' aria-hidden='true'></i>");
        } else {
            firstPara.slideUp("fast");
            secondPara.slideUp("fast");
            thirdPara.slideUp("fast");
            $(this).html("read more <i class='fa fa-angle-down' aria-hidden='true'></i>");
        }
    });
// Click On Sharing button to make Social Media Icons Show up
    var sharingIcons = $(".post-panel .social-media");
    sharingIcons.hide();
    $(".content-sharing").on("click", function (event) {
        event.preventDefault();
        if (sharingIcons.is(":hidden")) {
            sharingIcons.slideDown("fast");
        } else {
            sharingIcons.slideUp("fast");
        }
    });

// Click on checkbox to slidedown the FORM
    var diffrentForm = $(".another-form");
    diffrentForm.hide();
    $(".another-content input[type='checkbox']").on("click", function () {
        if (diffrentForm.is(":hidden")) {
            diffrentForm.slideDown("fast");
            $(".new-checkbox .true").css("opacity", "1");
        } else {
            diffrentForm.slideUp("fast");
            $(".new-checkbox .true").css("opacity", "0");
        }
    });
// Caching The Scroll Top Element
    var scrollButton = $("#scroll-top");
    $(window).scroll(function () {
        if ($(this).scrollTop() >= 730) {
            scrollButton.show();
        } else {
            scrollButton.hide();
        }
    });
// Click On fa-angle-top Button To Scroll Top
    scrollButton.click(function () {
        $("html,body").animate({scrollTop: 0}, 600);
    });

});