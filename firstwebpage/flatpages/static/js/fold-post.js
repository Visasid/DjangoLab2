var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++){
    { foldBtns[i].addEventListener("click", function(e) {
        console.log("you clicked ", e.target);

        if (e.target.className == "fold-button folded"){
            e.target.innerHTML = "Свернуть";
            e.target.className = "fold-button";
            e.target.parentElement.className = "one-post"
            var displayState = "block";
        }
        else{
            e.target.innerHTML = "Развернуть";
            e.target.className = "fold-button folded";
            e.target.parentElement.className = "one-post-folded"
            var displayState = "none";
        }
    }); 
    }
}