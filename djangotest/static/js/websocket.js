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
  let post_url = test.slice(0, -2) + data.post_id + '/'
  noti.innerHTML =
    `${data.message} - <a href="${post_url}"> 제목: [${data.title}]</a> `
  noti.classList.remove('invisible')
  noti.classList.remove('aos-animate')

  div.setAttribute('data-aos', 'flip-up')
  noti.append(div)
  setTimeout(() => {
    noti.classList.remove('aos-animate')
  }, 1000 * 15)
}
let noti = document.getElementById('newPostNoti')
noti.addEventListener('click', () => {
    noti.classList.remove('aos-animate')
  }
)