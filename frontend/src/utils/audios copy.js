class audios {
  constructor(arg) {
    this.audiosDom = {}
  }
  init() {

  }
  createAudioDom(option) {
    if (this.audiosDom[id]) {
      console.log(id, '已存在')
      return
    }
    let id = option.id + 'Audio';
    let audio = document.createElement('audio');
    audio.id = id;
    audio.src = option.src;
    audio.controls = true
    // audio.style.display = 'none';
    // audio.autoplay = true;
    let button = document.createElement('button');
    button.id = id + 'button';
    let that = this;
    button.onclick = function (isid) {
      console.log(isid, '555555555')
      console.log(that.audiosDom, '2222222222')
      console.log(isid, '2222222222')
      this.audiosDom[isid].audio.play()
    }
    document.body.appendChild(audio)
    document.body.appendChild(button)
    this.audiosDom[id] = {
      audio: audio,
      button: button,
    }
    // audio.onloadedmetadata = function () {
    if (option.state) {
      button.click(id)
      console.log(audio.paused)
    }
    // }
    // if (this.audiosDom[id]) {
    //   console.log(id, '已存在')
    // }

  }
}

export default audios
