document.addEventListener("DOMContentLoaded", function () {
    // Get canvas and set context
    const canvas = document.getElementById('animationCanvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    // Resize canvas when window size changes
    window.addEventListener('resize', function () {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    // Define particles for animation
    const particles = [];
    const colors = ['#00d4ff', '#ffffff', '#ff4081', '#a3ff00']; // Colors for particles

    // Create particle object
    function Particle(x, y, size, color, velocityX, velocityY) {
        this.x = x;
        this.y = y;
        this.size = size;
        this.color = color;
        this.velocityX = velocityX;
        this.velocityY = velocityY;

        // Update particle position
        this.update = function () {
            this.x += this.velocityX;
            this.y += this.velocityY;

            // Create a wrap-around effect
            if (this.x > width) this.x = 0;
            if (this.x < 0) this.x = width;
            if (this.y > height) this.y = 0;
            if (this.y < 0) this.y = height;

            this.draw();
        };

        // Draw the particle on canvas
        this.draw = function () {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
            ctx.closePath();
        };
    }

    // Initialize particles
    function initParticles() {
        particles.length = 0;
        const particleCount = 100; // Number of particles

        for (let i = 0; i < particleCount; i++) {
            const size = Math.random() * 4 + 1; // Random size between 1 and 5
            const x = Math.random() * width;
            const y = Math.random() * height;
            const color = colors[Math.floor(Math.random() * colors.length)];
            const velocityX = (Math.random() - 0.5) * 2; // Random horizontal speed
            const velocityY = (Math.random() - 0.5) * 2; // Random vertical speed

            particles.push(new Particle(x, y, size, color, velocityX, velocityY));
        }
    }

    // Animation loop
    function animate() {
        ctx.clearRect(0, 0, width, height);

        particles.forEach((particle) => {
            particle.update();
        });

        requestAnimationFrame(animate);
    }

    // Initialize and start the animation
    initParticles();
    animate();
});
