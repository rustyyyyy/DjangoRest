console.log("hello")

const posts = document.getElementById('posts')
const spinnerBox = document.getElementById('spinnerBox')
const loadbtn = document.getElementById('load-btn')

let visible = 3

const getData = () => {
    $.ajax({
        type: 'GET',
        url: `/data/${visible}/`,
        success: function(response) {
            const data = response.data
            setTimeout(() => {
                spinnerBox.classList.add('d-none')
                console.log(data)
                data.forEach(el => {
                    posts.innerHTML += `
                <div class="mb-3">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${el.title}</h5>
                            <p class="card-text">${el.body}</p>
                        </div>
                        <div class="card-footer">
                            <button class="btn btn-primary" type="button">Details</button>
                            <button class="btn btn-primary" type="button">like</button>
                        </div>
                    </div>
                </div>
                `
                });
            }, 100)
        },
        error: function(error) {
            console.log(error)
        }
    })
}

loadbtn.addEventListener('click', () => {
    spinnerBox.classList.remove('d-block')
    visible += 3
    getData()
})
getData()