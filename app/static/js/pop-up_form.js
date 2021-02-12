const popForm = document.getElementById('taskForm');
const formOpen = document.getElementById('addTask');
const formClose = document.getElementById('closeForm');

// when the user clicks on the button, open form
formOpen.onclick = () => {
  popForm.style.display = 'block';
}

// when the user clicks on the button, open form
formClose.onclick = () => {
  popForm.style.display = 'none';
}

// when the user clicks anywhere outside of the motal, close it
window.onclick = (event) => {
  if(event.target == popForm) {
    console.log('escondiendo popForm')
    popForm.style.display = 'none';
  }
}
