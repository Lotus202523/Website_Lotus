<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LOTUS 1st International Conference</title>
  <link rel="stylesheet" href="css/styles.css">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>html { scroll-behavior: smooth; }</style>
</head>
<body>
  <header>
    <div class="logo-header">
      <img src="images/logo1.png" alt="Logo Instansi">
      <img src="images/logo2.png" alt="Logo Negara">
    </div>
    <nav>
      <a href="#home">HOME</a>
      <div class="dropdown">
        <button>REGISTRATION</button>
        <div class="dropdown-content">
          <a href="#registration">Participants Registration</a>
          <a href="#registration">Presenter Registration</a>
          <a href="#registration">Abstract Submission</a>
        </div>
      </div>
      <a href="#committees">COMMITTEES</a>
      <a href="#proceedings">PROCEEDING</a>
    </nav>
  </header>

  <section id="home" class="hero">
    <div class="overlay">
      <h1>1st International Conference on Sustainable Tourism in Bali</h1>
      <p>July 31, 2025</p>
    </div>
  </section>

  <section id="about" class="container">
    <h2>About</h2>
    <p>This conference explores sustainable tourism through the lens of Tri Hita Karana, with Jatiluwih’s UNESCO subak irrigation as a model.</p>
    <div class="dates">
      <h3>Important Dates</h3>
      <ul>
        <li>21 July – Registration / Paper Submission opens</li>
        <li>30 July – Submission Deadline</li>
        <li>31 July – Conference Day</li>
      </ul>
    </div>
  </section>

  <section id="registration" class="container">
    <h2>Registration</h2>
    <div class="reg-buttons">
      <a href="YOUR_PARTICIPANT_LINK" class="button">Participants Registration</a>
      <a href="YOUR_PRESENTER_LINK" class="button">Presenter Registration</a>
      <a href="YOUR_ABSTRACT_LINK" class="button">Abstract Submission</a>
    </div>
    <div class="reg-info">
      <h3>Your conference registration includes:</h3>
      <ul>
        <li>E‑Certificate</li>
        <li>Proceeding for Paper and Abstract Submission</li>
        <li>SKP for Bali Tourism Institute Students</li>
      </ul>
    </div>
  </section>

  <section id="opening" class="container">
    <h2>Opening Remarks</h2>
    <div class="speaker">
      <img src="images/speaker-placeholder.png" alt="Opening Speaker">
      <p>Name, Title, Institution</p>
    </div>
  </section>

  <section id="keynotes" class="container">
    <h2>Keynote Speaker</h2>
    <div class="speaker">
      <img src="images/speaker-placeholder.png" alt="Keynote Speaker">
      <p>Name, Title, Institution — Topic Title</p>
    </div>
  </section>

  <section id="committees" class="container">
    <h2>Committees</h2>
    <div class="grid">
      <div class="committee">
        <img src="images/speaker-placeholder.png" alt="Committee">
        <p>Name<br>Institution</p>
      </div>
    </div>
  </section>

  <section id="proceedings" class="container">
    <h2>Proceedings</h2>
    <p>Proceedings will be published in indexed journal/ISBN book after peer review.</p>
    <a href="#" class="button">Download Proceedings</a>
  </section>

  <section id="partners" class="container logos-grid">
    <h2>Partners</h2>
    <a href="images/logo1.png" class="lightbox"><img src="images/logo1.png" alt="Partner Logo"></a>
    <a href="images/logo2.png" class="lightbox"><img src="images/logo2.png" alt="Partner Logo"></a>
  </section>

  <footer>
    <div class="logo-footer">
      <img src="images/logo1.png" alt="Logo Instansi">
      <img src="images/logo2.png" alt="Logo Negara">
    </div>
    <div class="contact">
      <p>Email: info@lotusconference.id | Phone: +62 123 4567 | Bali Tourism Institute</p>
    </div>
    <div class="footer-links">
      <a href="#">Privacy</a> | <a href="#">Terms</a>
    </div>
  </footer>

  <div id="modal" class="modal">
    <div class="modal-content">
      <span id="closeModal">&times;</span>
      <div id="modal-body"></div>
    </div>
  </div>

  <script>
    const modal = document.getElementById("modal");
    const modalBody = document.getElementById("modal-body");
    document.querySelectorAll(".speaker, .committee").forEach(el => {
      el.addEventListener("click", () => {
        const name = el.querySelector("p").innerText;
        modalBody.innerHTML = `<h3>${name}</h3><p>More details here...</p>`;
        modal.style.display = "flex";
      });
    });
    document.getElementById("closeModal").onclick = () => modal.style.display = "none";
    window.onclick = e => { if (e.target === modal) modal.style.display = "none"; };

    document.querySelectorAll('.lightbox').forEach(link => {
      link.onclick = e => {
        e.preventDefault();
        const overlay = document.createElement('div');
        overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);display:flex;justify-content:center;align-items:center;z-index:9999;';
        const img = document.createElement('img');
        img.src = link.href;
        img.style.maxWidth = '90%';
        img.style.maxHeight = '90%';
        overlay.appendChild(img);
        overlay.onclick = () => document.body.removeChild(overlay);
        document.body.appendChild(overlay);
      };
    });
  </script>
</body>
</html>

