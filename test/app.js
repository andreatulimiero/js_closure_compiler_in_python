$(document).foundation();
$(function(){
  console.log('Hi there');

  /* Menu */
  document.querySelector('nav .icon-menu').addEventListener('click', e => {
    var sideMenu = document.querySelector('nav .side');
    var topBar = document.querySelector('nav .mobile .topbar');
    if (sideMenu.classList.contains('opened')){
      sideMenu.classList.remove('opened');
      topBar.classList.remove('opened');
    }
    else{
      sideMenu.classList.add('opened');
      topBar.classList.add('opened');
    }
  });
  $('.mobile .side a').each(function(){
    $(this).click(function(){
      var sideMenu = document.querySelector('nav .side');
      var topBar = document.querySelector('.mobile .topbar');
      $('html body').animate({
        scrollTop: $($(this).attr('href')).offset().top - $('.mobile .topbar').height() 
      }, 600, 'swing');
      sideMenu.classList.remove('opened');
      topBar.classList.remove('opened');
      return false;
    });
  });
  $('.desktop .menu-titles a').each(function(){
    $(this).click(function(){
      var topBarHeight = $('.desktop').outerHeight();
      $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top - topBarHeight
      }, 600, 'swing');
      return false;
    });
  });
  $('.topbar .logo, .desktop .logo').click(function(){
    $('html, body').animate({
        scrollTop: 0
      }, 600, 'swing');
  });
  $('.side .logo').click(function(){
    $('.side').removeClass('opened');
    $('.topbar').removeClass('opened');
    $('html body').animate({
        scrollTop: 0
      }, 600, 'swing');
  });

  load_gallery();
  
});

function load_gallery(){
  $('[data-gallery]').click(function(){
    expand_image($(this).closest('.image-wrapper'));
  });
}

function expand_image(image_wrapper){
  $('[data-selected=true]').attr('data-selected', false);
  // Resizing image wrapper
  image_wrapper.attr('data-selected', 'true');
  //  Enabling close icon
  image_wrapper.find('.close').click(function(){
    collapse_image($(this).closest('.image-wrapper'));
  });
}

function collapse_image(image_wrapper){
  image_wrapper.attr('data-selected', false);
}