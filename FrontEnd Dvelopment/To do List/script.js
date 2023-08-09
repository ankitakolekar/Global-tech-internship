const inputBox = document.getElementById("inputBox")
const lsContainer = document.getElementById("lsContainer")


function addTask() {
    if(inputBox.value === "") {
        alert("You must write something !")
    }
    else {
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        lsContainer.appendChild(li)

        let span = document.createElement("span");
        span.innerHTML = '\u00d7';
        li.appendChild(span)
    }

    inputBox.value = ""
    todo();

    
}

lsContainer.addEventListener("click", function(e) {
    if(e.target.tagName === "LI") {
        e.target.classList.toggle("active");
        todo()
    }
    else if(e.target.tagName === "SPAN") {
        e.target.parentElement.remove();
        todo();
    }
}, false);

function todo() {
    localStorage.setItem("Todo", lsContainer.innerHTML);
}

function showTodo() {
    lsContainer.innerHTML = localStorage.getItem("Todo")
}

showTodo();