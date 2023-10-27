    const character = document.getElementById('character');
    const scoreDisplay = document.getElementById('score');
    let score = 0;
    let gameInterval;
    const gameContainer = document.getElementById('game-container');

    // Function to move the basket left to right
    function moveCharacter(event) {
      // Move left on left arrow key
      if (event.key === 'ArrowLeft') {
        const characterLeft = parseInt(getComputedStyle(character).left);
        if (characterLeft > 0) {
          character.style.left = (characterLeft - 30) + 'px';
        }
      //Move right on right arrow key event
      } else if (event.key === 'ArrowRight') {
        const characterLeft = parseInt(getComputedStyle(character).left);
        if (characterLeft < (gameContainer.clientWidth - character.clientWidth)) {
          character.style.left = (characterLeft + 30) + 'px';
        }
      }
    }

    // Simulate the objects falling from the above
    function createFallingObject() {
      const fallingObject = document.createElement('div');
      fallingObject.classList.add('falling-object');
      fallingObject.style.left = Math.random() * (gameContainer.clientWidth - 20) + 'px';
      let num = Math.floor(Math.random() *7)+1;
      fallingObject.innerHTML =`<img src="./images/${num}.png" alt=""></img>`;
      gameContainer.appendChild(fallingObject);


      const fallInterval = setInterval(() => {
        const topPosition = parseInt(getComputedStyle(fallingObject).top);
        fallingObject.style.top = (topPosition + 5) + 'px';

        if (topPosition > (gameContainer.clientHeight - fallingObject.clientHeight)) {
          clearInterval(fallInterval);
          gameContainer.removeChild(fallingObject);
        }

        const characterLeft = parseInt(getComputedStyle(character).left);
        const characterRight = characterLeft + character.clientWidth;
        const objectLeft = parseInt(getComputedStyle(fallingObject).left);
        const objectRight = objectLeft + fallingObject.clientWidth;

        if (topPosition >= (gameContainer.clientHeight - fallingObject.clientHeight - character.clientHeight) &&
            characterLeft <= objectRight && characterRight >= objectLeft) {
          gameContainer.removeChild(fallingObject);
          if(num==7){
            score -= 10;
          }
          else{
            score += 10;
          }
          scoreDisplay.textContent = 'Score: ' + score;
        }
      }, 20);
    }

    // Game Start function
    function startGame() {
      score = 0;
      scoreDisplay.textContent = 'Score: 0';
      character.style.left = '50%';
      gameInterval = setInterval(createFallingObject, 1000);
      window.addEventListener('keydown', moveCharacter);
    }

    // Game over function
    function endGame() {
      clearInterval(gameInterval);
      window.removeEventListener('keydown', moveCharacter);
      
    }
    startGame();
    runTimer();
    {/*  Game duration: 30 seconds */}
    timer = 30;
    function runTimer(){
        var timerInterval = setInterval(function(){
            if(timer>0){
                timer--;
                document.querySelector("#timerVal").textContent = `Timer: ${timer}`;
            }
            else{
                clearInterval(timerInterval);
                document.body.innerHTML=`<div class = "game-over"><h1> Game Over!<br>Your Score: ${score}</h1></div> <a href="index.html"><button class="button2">Exit</button></button></a> `;
            }
            
        },1000);
    }