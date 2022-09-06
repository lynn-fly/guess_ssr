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
    let button = document.createElement('button');
    button.style.display = 'none';
    audio.id = id;
    audio.src = option.src;
    audio.controls = true
    audio.style.display = 'none';
    if (option.state) {
      audio.autoplay = true;
    }
    audio['webkit-playsinline'] = true;
    audio.loop = option.loop || false;
    document.body.appendChild(audio)
    this.audiosDom[id] = audio;
    // audio.onloadedmetadata = function () {
    button.click()
    if (option.state) {
      setTimeout(() => {
        audio.play()
      }, 100);
    }
    // }
  }
  play(id) {
    if (this.audiosDom[id + 'Audio'].paused) {
      this.audiosDom[id + 'Audio'].play()
    }
  }
  pause(id) {
    if (!this.audiosDom[id + 'Audio'].paused) {
      this.audiosDom[id + 'Audio'].pause()
    }
  }
  getPause(id) {
    console.log(this.audiosDom[id + 'Audio'])
    return this.audiosDom[id + 'Audio'].paused
  }
}

export default audios
