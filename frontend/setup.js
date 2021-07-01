class Setup {
  static fields() {
    return Array.from(document.querySelectorAll('#setup .content input')).map(el => el.id);
  }

  static load() {
    Setup.fields().forEach(field => {
      document.querySelector(`#${field}`).value = localStorage.getItem(field);
    });
  }

  static save() {
    Setup.fields().forEach(field => {
      localStorage.setItem(field, document.querySelector(`#${field}`).value);
    });
  }

  static toggle() {
    $('#setup .content').toggle();
  }
}

Setup.load();
