/*

=========================================================
* Pixel Free Bootstrap 5 UI Kit
=========================================================

* Product Page: https://themesberg.com/product/ui-kit/pixel-free-bootstrap-5-ui-kit
* Copyright 2021 Themesberg (https://www.themesberg.com)

* Coded by https://themesberg.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. Contact us if you want to remove it.

*/

"use strict";
const d = document;
d.addEventListener("DOMContentLoaded", function(event) {

    // options
    const breakpoints = {
        sm: 540,
        md: 720,
        lg: 960,
        xl: 1140
    };
    
    var preloader = d.querySelector('.preloader');
    if(preloader) {

        const animations = ['oneByOne', 'delayed', 'sync', 'scenario'];

        new Vivus('loader-logo', {duration: 80, type: 'oneByOne'}, function () {});

        setTimeout(function() {
            preloader.classList.add('show');
        }, 1500);
    }

    if (d.querySelector('.headroom')) {
        var headroom = new Headroom(document.querySelector("#navbar-main"), {
            offset: 0,
            tolerance: {
                up: 0,
                down: 0
            },
        });
        headroom.init();
    }

    // dropdowns to show on hover when desktop
    if (d.body.clientWidth > breakpoints.lg) {
        var dropdownElementList = [].slice.call(document.querySelectorAll('.navbar .dropdown-toggle'))
        dropdownElementList.map(function (dropdownToggleEl) {
            var dropdown = new bootstrap.Dropdown(dropdownToggleEl);
            var dropdownMenu = d.querySelector('.dropdown-menu[aria-labelledby="' + dropdownToggleEl.getAttribute('id') + '"]');

            dropdownToggleEl.addEventListener('mouseover', function () {
                dropdown.show();
            });
            dropdownToggleEl.addEventListener('mouseout', function () {
                dropdown.hide();
            });

            dropdownMenu.addEventListener('mouseover', function () {
                dropdown.show();
            });

            dropdownMenu.addEventListener('mouseout', function () {
                dropdown.hide();
            });
            
        });
    }

    [].slice.call(d.querySelectorAll('[data-background]')).map(function(el) {
        el.style.background = 'url(' + el.getAttribute('data-background') + ')';
    });

    [].slice.call(d.querySelectorAll('[data-background-color]')).map(function(el) {
        el.style.background = 'url(' + el.getAttribute('data-background-color') + ')';
    });

    [].slice.call(d.querySelectorAll('[data-color]')).map(function(el) {
        el.style.color = 'url(' + el.getAttribute('data-color') + ')';
    });

    // Tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    // Popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
      return new bootstrap.Popover(popoverTriggerEl)
    })

    // Datepicker
    var datepickers = [].slice.call(document.querySelectorAll('[data-datepicker]'))
    var datepickersList = datepickers.map(function (el) {
        return new Datepicker(el, {
            buttonClass: 'btn'
          });
    })

    // Toasts
    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl)
    })

    var scroll = new SmoothScroll('a[href*="#"]', {
        speed: 500,
        speedAsDuration: true
    });

    if (d.querySelector('.current-year')) {
        d.querySelector('.current-year').textContent = new Date().getFullYear();
    }

});


const Annually = document.querySelector('#Annually')
const monthly = document.querySelector('#monthly')
function viewPaymetAnnually() {
    Annually.style.display = "none"
    monthly.style.display = "flex"

}
function viewPaymetmonthly() {
    monthly.style.display = "none"
    Annually.style.display = "flex"

}

document.querySelectorAll(".output").forEach((item, index) => {
    console.log(index)
    item.addEventListener("click", async (event) => {

        let selectItem = event.path[3].querySelector(".txtdata");
        try {
            await navigator.clipboard.writeText(selectItem.querySelector("p").innerHTML.replace('<br>','\n'));
            alert("Copied to clipboard");

        } catch (err) {
            console.error("Failed to copy!", err);
        }
    });
});



var slider = document.getElementById("rang1");
var output = document.getElementById("count");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}


const loader = document.getSelection('.loader')
const loaderitem_1 = document.getSelection('.inf-text')
const loaderitem_2 = document.getSelection('.overflowData')

function loaderPopa() {
    loaderitem_1.style.display ='none'
}



function show_pw() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

















