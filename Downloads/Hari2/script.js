document.addEventListener("DOMContentLoaded", function() {
  var sideMenu = document.getElementById("sidemenu");
  var navToggle = document.getElementById("nav-toggle");
  var closeBtn = document.getElementById("closebtn");

  navToggle.addEventListener("click", function() {
    sideMenu.style.right = "0";
  });

  closeBtn.addEventListener("click", function() {
    sideMenu.style.right = "-200px";
  });
});
