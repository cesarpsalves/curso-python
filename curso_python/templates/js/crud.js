let usuarios = JSON.parse(localStorage.getItem("usuarios") || "[]");
let indexEditar = -1;

function salvarDados() {
  localStorage.setItem("usuarios", JSON.stringify(usuarios));
}

function atualizarTabela() {
  const corpo = document.getElementById("tabela-usuarios");
  if (!corpo) return;
  corpo.innerHTML = "";
  usuarios.forEach((u, i) => {
    corpo.innerHTML += `
      <tr>
        <td>${u.username}</td>
        <td>${u.nome}</td>
        <td>${u.sobrenome}</td>
        <td class="text-center">
          <a href="editar.html?id=${i}" class="text-primary me-2">✏️</a>
          <a href="#" onclick="excluirUsuario(${i})" class="text-danger">🗑️</a>
        </td>
      </tr>`;
  });
}

function excluirUsuario(index) {
  if (confirm("Deseja realmente excluir este usuário?")) {
    usuarios.splice(index, 1);
    salvarDados();
    atualizarTabela();
  }
}

document.addEventListener("DOMContentLoaded", function () {
  if (document.getElementById("form-inserir")) {
    document.getElementById("form-inserir").addEventListener("submit", function (e) {
      e.preventDefault();
      const username = document.getElementById("username").value;
      const nome = document.getElementById("nome").value;
      const sobrenome = document.getElementById("sobrenome").value;
      usuarios.push({ username, nome, sobrenome });
      salvarDados();
      window.location.href = "index.html";
    });
  }

  if (document.getElementById("form-editar")) {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    if (id !== null && usuarios[id]) {
      document.getElementById("id-editar").value = id;
      document.getElementById("username-editar").value = usuarios[id].username;
      document.getElementById("nome-editar").value = usuarios[id].nome;
      document.getElementById("sobrenome-editar").value = usuarios[id].sobrenome;
    }
    document.getElementById("form-editar").addEventListener("submit", function (e) {
      e.preventDefault();
      const idx = document.getElementById("id-editar").value;
      usuarios[idx] = {
        username: document.getElementById("username-editar").value,
        nome: document.getElementById("nome-editar").value,
        sobrenome: document.getElementById("sobrenome-editar").value
      };
      salvarDados();
      window.location.href = "index.html";
    });
  }

  atualizarTabela();
});
