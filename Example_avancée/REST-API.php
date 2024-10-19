<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recherche Photos Instagram</title>
    <link rel="stylesheet" href="styles.css"> <!-- Lien vers le fichier CSS -->
</head>
<body>
    <h1>Recherche Photos Instagram par Ville</h1>
    <form method="POST" action="index.php">
        <label for="city">Nom de la ville :</label>
        <input type="text" id="city" name="city" required>
        <button type="submit">Rechercher</button>
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $city = htmlspecialchars($_POST['city']);
        displayInstagramPhotos($city);
    }

    function getCityCoordinates($city) {
        $apiKey = 'YOUR_GOOGLE_MAPS_API_KEY'; // Remplace par ta clé API Google Maps
        $url = "https://maps.googleapis.com/maps/api/geocode/json?address=" . urlencode($city) . "&key=" . $apiKey;
        
        $response = file_get_contents($url);
        $data = json_decode($response, true);
        
        if (isset($data['results'][0])) {
            return $data['results'][0]['geometry']['location'];
        } else {
            return null;
        }
    }

    function getInstagramPhotos($latitude, $longitude) {
        $accessToken = 'YOUR_INSTAGRAM_ACCESS_TOKEN'; // Remplace par ton token d'accès Instagram
        $url = "https://graph.instagram.com/me/media?fields=id,caption,media_url,thumbnail_url,permalink&access_token=" . $accessToken;

        $response = file_get_contents($url);
        $data = json_decode($response, true);
        
        $photos = [];
        foreach ($data['data'] as $photo) {
            // Si tu veux filtrer les photos par coordonnées, ajoute ta logique ici
            $photos[] = $photo;
        }
        return $photos;
    }

    function displayInstagramPhotos($city) {
        $coordinates = getCityCoordinates($city);

        if ($coordinates) {
            $latitude = $coordinates['lat'];
            $longitude = $coordinates['lng'];

            $photos = getInstagramPhotos($latitude, $longitude);

            if (empty($photos)) {
                echo "<p>Aucune photo trouvée pour cette ville.</p>";
            } else {
                echo "<h2>Photos Instagram à $city :</h2>";
                foreach ($photos as $photo) {
                    echo "<div class='photo'>";
                    echo "<a href='{$photo['permalink']}' target='_blank'><img src='{$photo['media_url']}' alt='Photo'></a>";
                    echo "<p>{$photo['caption']}</p>";
                    echo "</div>";
                }
            }
        } else {
            echo "<p>Coordonnées non trouvées pour la ville : $city.</p>";
        }
    }
    ?>
</body>
</html>
