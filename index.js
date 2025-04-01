console.log('Hello World')

const testEl =document.getElementById('test-el')

testEl.textContent ='bye bye'

testEl.addEventListener('click', () => {
    console.log('clicked');
    testEl.innerHTML = '<b>clicked</b>';
})

testEl.addEventListener('mouseover', () => {
    console.log('on');
})
  
testEl.addEventListener('mouseout', () => {
    console.log('off');
})


document.addEventListener('scroll', () => {
    const positionY =window.scrollY
    console.log(positionY)
})

// GET the data with ajax
const url = 'https://swapi.dev/api/people/';

// 1. jquery ajax method <- this is what we are going to use in this course
$.ajax({
    type: 'GET',
    url: url,
    success: function(response) {
      console.log('jquery ajax', response)
    },
    error: function(error) {
      console.log(error)
    }
  })
// 2. XMLHttpRequest



// 3. fetch method

// other popular: axios library, async await + fetch