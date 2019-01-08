window.addEventListener('load', () => {
  let nSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/notification/'
  )
  let notificationStack = []
  nSocket.onclose = function (e) {
    console.error('noti socket closed')
  }

  nSocket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    let noti = document.getElementById('newPostNoti')
    let div = document.createElement('div')
    let post_url = post_detail_url.slice(0, -2) + data.post_id + '/'

    if (noti.childNodes.length > 2) {
      let firstNoti = notificationStack.shift()
      let delDiv = document.getElementById(firstNoti)
      noti.removeChild(delDiv)
    }

    noti.classList.remove('invisible')
    noti.classList.remove('aos-animate')

    div.setAttribute('data-aos', 'flip-up')
    div.setAttribute('id', `${data.post_id}`)
    div.classList.add('noti-solo')

    notificationStack.push(data.post_id)

    div.innerHTML =
      `${data.message} - <a href="${post_url}"> [제목: ${data.title}]</a> `
    noti.appendChild(div)
  }

  let noti = document.getElementById('newPostNoti')
  noti.addEventListener('click', () => {
      noti.classList.remove('aos-animate')
      notificationStack.forEach(n => {
        let del = document.getElementById(n)
        noti.removeChild(del)
      })

    }
  )
})