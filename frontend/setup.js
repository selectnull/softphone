/* jshint esversion: 6 */

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

  static asCode() {
    let code = '';
    Setup.fields().forEach(field => {
      let value = localStorage.getItem(field);
      code += `localStorage.setItem(${field}, "${value}");\n`;
    });
    return code;
  }
}

Setup.load();
