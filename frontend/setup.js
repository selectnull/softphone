class Setup {
  static fields = ['apiUsername', 'apiPassword', 'webrtcUsername', 'webrtcPassword', 'phoneNumber'];

  static load() {
    Setup.fields.forEach(field => {
      document.querySelector(`#${field}`).value = localStorage.getItem(field);
    });
  }

  static save() {
    Setup.fields.forEach(field => {
      localStorage.setItem(field, document.querySelector(`#${field}`).value);
    });

  }
}

Setup.load();
