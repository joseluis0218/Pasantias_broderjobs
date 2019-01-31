/*************************************
@@File: Job Stock  Template Custom Js

All custom js files contents are below
**************************************
* 01. Company Brand Carousel
* 02. Client Story testimonial
* 03. Bootstrap wysihtml5 editor
* 04. Tab Js
* 05. Add field Script
**************************************/

(function($){
"use strict";
	$("#company-brands").owlCarousel({
		loop: true,
		autoplay: true,
		autoplayTimeout:1000,
		responsiveClass: true,
		margin: 30,	
		responsive: {
			0: {
				items: 2,
				stagePadding:40,
				margin: 30,				
			},
			600: {
				items: 3,
			},
			1000: {
				items: 4,
			},
			1200: {
				items: 5,
			}
		}
	});

	 /*---Company Brand Carousel --*/
	 $("#company-brands2").owlCarousel({
		items:5,
		itemsDesktop:[1199,5],
		itemsDesktopSmall:[979,4],
		itemsTablet:[768,3],
		itemsMobile: [600, 2],
		pagination: false,
		navigation: false,
		navigationText:["",""],
		autoPlay: 2000,
		stopOnHover: true,
		transitionStyle: true
	});
	
	/*--- Client Story testimonial --*/
	$("#client-testimonial-slider").owlCarousel({
		items:3,
		loop: true,
		autoplay: true,
		pagination: false,
		navigation:false,
		itemsMobile: [600, 1],
		navigationText:["",""],
		autoPlay: true,
		stopOnHover: true,
		responsive: {
			0: {
				items: 1
			},
			600:{
				items:1
			},
			1200: {
				items: 3
			}
		}
	});
	
	/*---Bootstrap wysihtml5 editor --*/	
	$('.textarea').wysihtml5();
	
	/*---Tab Js --*/
	$("#simple-design-tab a").on('click', function(e){
				e.preventDefault();
				$(this).tab('show');
	});
	
	/*-----Add field Script------*/
	$('.extra-field-box').each(function() {
    var $wrapp = $('.multi-box', this);
    $(".add-field", $(this)).on('click', function() {
        $('.dublicat-box:first-child', $wrapp).clone(true).appendTo($wrapp).find('input').val('').focus();
    });
    $('.dublicat-box .remove-field', $wrapp).on('click', function() {
        if ($('.dublicat-box', $wrapp).length > 1)
            $(this).parent('.dublicat-box').remove();
		});
	});
			
			
	})(jQuery);