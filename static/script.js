const canvas = document.getElementById('backgroundCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Function to create background animation
function animateBackground() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
    gradient.addColorStop(0, 'rgba(0, 102, 204, 0.5)');
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0.5)');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < 50; i++) {
        ctx.beginPath();
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height;
        const radius = Math.random() * 2 + 1;
        ctx.arc(x, y, radius, 0, Math.PI * 2, false);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        ctx.fill();
    }

    requestAnimationFrame(animateBackground);
}

// Start animation
animateBackground();

// Handle weather form submission
document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const city = document.getElementById('city').value;
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('weatherResult').innerText = data.error;
            } else {
                document.getElementById('weatherResult').innerText = `
                    Weather in ${data.name}: ${data.weather}
                    Temperature: ${data.main.temp} °C
                    Humidity: ${data.main.humidity}%
                    Wind Speed: ${data.wind.speed} m/s
                `;
            }
        })
        .catch(error => {
            document.getElementById('weatherResult').innerText = "Error fetching weather data.";
        });
});
