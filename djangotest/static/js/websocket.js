let nSocket = new WebSocket(
  'ws://' + window.location.host + '/ws/notification/'
)

nSocket.onclose = function (e) {
  console.error('noti socket closed')
}

nSocket.onmessage = function (e) {
  let data = JSON.parse(e.data)
  let noti = document.getElementById('newPostNoti')
  let div = document.createElement('div')
  noti.innerText = data.message
  noti.classList.remove('invisible')
  noti.classList.remove('aos-animate')

  div.setAttribute('data-aos', 'flip-up')
  noti.append(div)
  setTimeout(() => {
    noti.classList.remove('invisible')
    noti.classList.remove('aos-animate')
  }, 5000)
}
let noti = document.getElementById('newPostNoti')
noti.addEventListener('click', () => {
  noti.classList.remove('aos-animate')
  }
)