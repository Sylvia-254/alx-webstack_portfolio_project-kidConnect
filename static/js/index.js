const  body = document.getElementsByTagName("body")[0]

function setcolor(name){
    body.style.backgroundcolor = name;
}

function randomcolor(){
     const red = math.round(math.random)() * 255 
     const blue = math.round(math.random)() * 255 
     const green = math.round(math.random)() * 255 
     
     const color = `rgb(${red}, ${green}, ${blue})`
     body.style.backgroundcolor = color;
}

randomcolor()