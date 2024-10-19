const apiKey = 'YOUR_API_KEY'; // Remplace par ta clé API OpenWeatherMap
const getWeatherBtn = document.getElementById('getWeatherBtn');
const weatherInfo = document.getElementById('weatherInfo');

getWeatherBtn.addEventListener('click', () => {
    const cityInput = document.getElementById('cityInput').value;
    getWeather(cityInput);
});

function getWeather(city) {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`; // Utilise "units=metric" pour la température en Celsius

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Ville non trouvée');
            }
            return response.json();
        })
        .then(data => {
            const cityName = data.name;
            const temperature = data.main.temp;
            const weatherDescription = data.weather[0].description;

            displayWeather(cityName, temperature, weatherDescription);
        })
        .catch(error => {
            weatherInfo.innerHTML = `<p>${error.message}</p>`;
        });
}

function displayWeather(cityName, temperature, description) {
    weatherInfo.innerHTML = `
        <h2>Météo à ${cityName}</h2>
        <p>Température : ${temperature} °C</p>
        <p>Description : ${description}</p>
    `;
}
