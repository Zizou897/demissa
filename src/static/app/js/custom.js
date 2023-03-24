// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 2
        }
    }
});



/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

/* */

window.addEventListener('scroll', function() {
    let header = document.querySelector('.a-nav');
    let windowPosition = window.pageYOffset > 600 ;
    header.classList.toggle('scrolling-active', windowPosition);            
})

let mainListDiv = document.getElementById("mainListDiv"),
mediaButton = document.getElementById("mediaButton"),
navbar = document.querySelector('.nav');

mediaButton.onclick = function () {
 
    mainListDiv.style.transition = "all 0.8s ease-in-out";
    mainListDiv.classList.toggle("show_list");
    mediaButton.classList.toggle("active");
};


let icon = document.querySelector(".search");
let input = document.querySelector(" .inputsearch");

icon.addEventListener("click", (e) => {
  e.preventDefault();
   if (input.style.display === "none") {
    input.style.display = "block";
  } else {
    input.style.display = "none";
  }
});


// for payment

window.addEventListener('DOMContentLoaded', ()=>{
    const codepromo = document.querySelector(".codepromo")
    const date = document.querySelector("input[type='date']")
    const time = document.querySelector("input[type='time']")
    const submit = document.querySelector(".submit")
    const inputImages = document.querySelectorAll("input[type='file']")
    const deletes = document.querySelectorAll(".delete")

    const minDate = new Date().toLocaleDateString().split('/').reverse().join('-')
    const hoursTwo = parseInt(new Date().toLocaleString().split(' ')[1].split(':').shift()) + 2
    const minHour = new Date().toLocaleString().split(' ')[1].split(':').slice(0, 2).fill(hoursTwo, 0, 1).join(':')
    date.min = minDate
    date.value = minDate
    time.value = minHour


    codepromo.addEventListener('click', (e)=>{
        const code = e.target.previousElementSibling.value
        console.log('codepromo', code)
        //faire le traitement sur le cocepromo
    })

    Array.from(inputImages).map(input=>{
        input.addEventListener('change', (e)=>{
            const parent = e.target.closest('.upload-item')
            const image = e.target.previousElementSibling.previousElementSibling.firstElementChild
            const previewUrl = URL.createObjectURL(e.target.files[0])
            image.src = previewUrl
            parent.classList.add('active')
        })
    })

    Array.from(deletes).map(del=>{
        del.addEventListener('click', (e)=>{
            const parent = e.target.closest(".upload-item")
            const file = parent.lastElementChild
            parent.classList.remove('active')
            file.value = ''
        })
    })

    submit.addEventListener('click', (e)=>{
        // faire le traitement quand on soumet le formulaire 
    })

})

// for Menu
