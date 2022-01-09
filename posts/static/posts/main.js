const posts = document.getElementById("posts");
const spinnerBox = document.getElementById("spinnerBox");
const loadbtn = document.getElementById("load-btn");
const endBox = document.getElementById("endBox");


const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const likeUnlikePosts = () =>{
  const likeUnlikeForms = [...document.getElementsByClassName('like-unlike-forms')]
  likeUnlikeForms.forEach(form => form.addEventListener('submit', e=>{
      e.preventDefault()
      const clickedId = e.target.getAttribute('data-form-id')
      const clickedBtn = document.getElementById(`like-unlike-${clickedId}`)

      $.ajax({
          type:'POST',
          url:'/like-unlike/',
          data: {
            'csrfmiddlewaretoken' : csrftoken,
            'pk' : clickedId,
          },
          success: function(response){
              console.log(response)
              clickedBtn.textContent = response.liked ? `Unlike (${response.count})` : `like (${response.count})`
          },
          error: function(error){
            console.log(error)
          }

      })
  }))
}

let visible = 3;

const getData = () => {
  $.ajax({
    type: "GET",
    url: `/data/${visible}/`,
    success: function (response) {
      const data = response.data;
      setTimeout(() => {
        spinnerBox.classList.add("d-none");
        // console.log(data)
        data.forEach((el) => {
          posts.innerHTML += `
          <div class="mb-3">
              <div class="card">
                  <div class="card-body">
                      <h5 class="card-title">${el.title}</h5>
                      <p class="card-text">${el.body}</p>
                  </div>
                  <div class="card-footer">
                      <button class="btn btn-primary" type="button">Details</button>
                      
                      <form class="like-unlike-forms" data-form-id="${el.id}">
                        <button id="like-unlike-${el.id}" class="btn btn-primary" type="submit">${
                          el.liked ? `Unlike (${el.count})` : `like (${el.count})`
                        }</button>
                      </form>
                  </div>
              </div>
            </div>  
          `;
        });
        likeUnlikePosts()
      }, 100);
          console.log(response.size);
          if (response.size === 0) {
            endBox.textContent = "No posts added yet";
          } else if (response.size <= visible) {
            loadbtn.classList.add("d-none");
            endBox.textContent = "end of posts";
          }
    },
    error: function (error) {
      console.log(error);
    },
  });
};

loadbtn.addEventListener("click", () => {
  spinnerBox.classList.remove("d-block");
  visible += 3;
  getData();
});
getData();
