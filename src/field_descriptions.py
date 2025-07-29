DESCRIPTIONS = {
    "meta": "Sezione contenente informazioni generali e identificative sull'immagine generata.",
    # --- META FIELDS (user-editability and system notes) ---
    "meta.promptId": (
        "Identificatore univoco della richiesta di generazione, ad esempio 'IMG_2025_001'. "
        "Campo gestito automaticamente dal sistema e non modificabile dall'utente."
    ),
    "meta.schemaVersion": (
        "Versione dello schema dati utilizzato per il prompt, ad esempio '1.0'. "
        "Campo gestito automaticamente dal sistema e non modificabile dall'utente."
    ),
    "meta.createdAt": (
        "Data e ora di creazione del prompt in formato ISO 8601, ad esempio '2024-04-27T15:30:00Z'. "
        "Campo generato automaticamente dal sistema e non modificabile dall'utente."
    ),
    "meta.updatedAt": (
        "Data e ora dell'ultima modifica del prompt in formato ISO 8601, ad esempio '2024-04-28T12:10:00Z'. "
        "Campo gestito automaticamente dal sistema e non modificabile dall'utente."
    ),
    "meta.generationSeed": (
        "Valore seed utilizzato per la generazione casuale dell'immagine, utile per riproducibilità. "
        "Campo gestito dal sistema, non modificabile dall'utente."
    ),
    "meta.version": (
        "Versione del prompt o del modello utilizzato, ad esempio 'v1.0'. "
        "Campo gestito dal sistema e non modificabile direttamente dall'utente."
    ),
    "meta.author": (
        "Nome o identificatore dell'autore della richiesta, ad esempio 'utente123'. "
        "Campo gestito dal sistema; può essere impostato al momento della creazione ma generalmente non modificato manualmente."
    ),
    "meta.title": (
        "Titolo descrittivo dell'immagine o del prompt. "
        "Campo modificabile dall'utente. "
        "Esempi: 'Ritratto al tramonto', 'Paesaggio urbano futuristico'."
    ),
    "meta.tags": (
        "Lista di parole chiave associate all'immagine per facilitarne la ricerca e la categorizzazione. "
        "Campo modificabile dall'utente. "
        "Esempi: ['ritratto', 'tramonto', 'HDR', 'urbano']."
    ),
    "meta.aspectRatio": (
        "Rapporto tra larghezza e altezza dell'immagine. "
        "Campo modificabile dall'utente. "
        "Valori accettati: stringa nel formato '16:9', '4:3', '1:1', ecc."
    ),
    "meta.orientation": (
        "Orientamento dell'immagine. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'orizzontale', 'verticale', 'quadrato'."
    ),
    "meta.colorProfile": (
        "Profilo colore utilizzato per l'immagine. "
        "Campo modificabile dall'utente. "
        "Esempi: 'sRGB', 'AdobeRGB', 'ProPhotoRGB'."
    ),
    "meta.dpi": (
        "Risoluzione di stampa dell'immagine in punti per pollice (DPI). "
        "Campo modificabile dall'utente. "
        "Valori comuni: 72, 150, 300."
    ),
    "meta.category": (
        "Categoria tematica dell'immagine. "
        "Campo modificabile dall'utente. "
        "Esempi: 'ritratto', 'paesaggio', 'astratto', 'architettura'."
    ),

    "camera": "Parametri della fotocamera virtuale utilizzata per catturare l'immagine.",
    "camera.brand": (
        "Marca della fotocamera. "
        "Campo modificabile dall'utente. "
        "Esempi: 'Canon', 'Nikon', 'Sony'."
    ),
    "camera.model": (
        "Modello specifico della fotocamera. "
        "Campo modificabile dall'utente. "
        "Esempi: 'EOS R5', 'D850', 'Alpha 7 IV'."
    ),
    "camera.sensorFormat": (
        "Formato del sensore della fotocamera. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'Full Frame', 'APS-C', 'Micro Four Thirds', ecc."
    ),
    "camera.lensType": (
        "Tipo di lente utilizzata. "
        "Campo modificabile dall'utente. "
        "Esempi: 'prime', 'zoom', 'macro', 'teleobiettivo'."
    ),
    "camera.lensModel": (
        "Modello specifico della lente. "
        "Campo modificabile dall'utente. "
        "Esempi: 'EF 24-70mm f/2.8L', 'AF-S 85mm f/1.4'."
    ),
    "camera.focalLength": (
        "Lunghezza focale della lente in millimetri. "
        "Campo modificabile dall'utente. "
        "Valori tipici da 10 a 200. Esempi: 35, 50, 85."
    ),
    "camera.aperture": (
        "Apertura del diaframma indicata come numero f-stop. "
        "Campo modificabile dall'utente. "
        "Valori comuni da f/1.2 a f/22. Esempi: 1.8, 4.0."
    ),
    "camera.shutterSpeed": (
        "Velocità dell'otturatore in secondi o frazioni di secondo. "
        "Campo modificabile dall'utente. "
        "Formati accettati: '1/125', '0.5'."
    ),
    "camera.iso": (
        "Sensibilità ISO della fotocamera. "
        "Campo modificabile dall'utente. "
        "Valori tipici da 100 a 6400."
    ),
    "camera.whiteBalance": (
        "Impostazione del bilanciamento del bianco. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'Auto', 'Daylight', 'Cloudy', 'Tungsten', 'Fluorescent', ecc."
    ),
    "camera.meteringMode": (
        "Modalità di misurazione dell'esposizione. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'Matrix', 'Center-weighted', 'Spot'."
    ),
    "camera.focusMode": (
        "Modalità di messa a fuoco. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'Manual', 'Auto', 'Continuous'."
    ),
    "camera.imageStabilization": (
        "Indica se la stabilizzazione dell'immagine è attiva. "
        "Campo modificabile dall'utente. "
        "Valori booleani: true o false."
    ),
    "camera.angle": (
        "Angolo di ripresa della fotocamera in gradi. "
        "Campo modificabile dall'utente. "
        "Valori numerici da 0 a 360."
    ),
    "camera.perspective": (
        "Tipo di prospettiva utilizzata. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'normale', 'grandangolo', 'teleobiettivo', 'fish-eye'."
    ),
    "camera.captureType": (
        "Tipo di cattura dell'immagine. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'singola', 'raffica', 'HDR', 'panorama'."
    ),
    "camera.cameraMovement": (
        "Tipo di movimento della fotocamera durante la cattura. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'statico', 'panoramica', 'tilt', 'dolly', 'zoom'."
    ),
    "camera.distanceFromSubject": (
        "Distanza dalla fotocamera al soggetto in metri. "
        "Campo modificabile dall'utente. "
        "Valori numerici positivi. Esempi: 1.5, 10."
    ),
    "camera.viewAngle": (
        "Angolo di campo della fotocamera in gradi. "
        "Campo modificabile dall'utente. "
        "Valori numerici da 10 a 120."
    ),
    "camera.captureTypeOptions": (
        "Opzioni specifiche per il tipo di cattura scelto. "
        "Campo modificabile dall'utente. "
        "Esempi: {'HDR': {'exposures': 3, 'bracket': true}}."
    ),
    "camera.focalLengthRange": (
        "Intervallo di lunghezze focali per l'obiettivo zoom in millimetri. "
        "Campo modificabile dall'utente. "
        "Formato: [min, max], esempio: [24, 70]."
    ),
    "camera.apertureRange": (
        "Intervallo di aperture disponibili per l'obiettivo. "
        "Campo modificabile dall'utente. "
        "Formato: [min, max], esempio: [1.8, 22]."
    ),
    "camera.qualitySettings": "Impostazioni di qualità della fotocamera virtuale.",
    "camera.qualitySettings.noiseReduction": (
        "Livello di riduzione del rumore applicato. "
        "Campo modificabile dall'utente. "
        "Valori numerici da 0 (nessuna riduzione) a 1 (massima riduzione)."
    ),
    "camera.qualitySettings.dynamicRange": (
        "Gamma dinamica della fotocamera. "
        "Campo modificabile dall'utente. "
        "Valori numerici positivi, es. 14."
    ),
    "camera.qualitySettings.colorDepth": (
        "Profondità di colore in bit per canale. "
        "Campo modificabile dall'utente. "
        "Valori comuni: 8, 10, 12."
    ),
    "camera.qualitySettings.lensDistortion": (
        "Coefficiente di distorsione della lente. "
        "Campo modificabile dall'utente. "
        "Valori numerici, dove 0 indica nessuna distorsione."
    ),

    "subjects": "Elenco dei soggetti presenti nell'immagine.",
    "subjects[].descriptor": (
        "Descrizione breve del soggetto. "
        "Campo obbligatorio. "
        "Esempi: 'ragazza sorridente', 'uomo anziano', 'cane al guinzaglio'."
    ),
    "subjects[].ageGroup": (
        "Fascia d'età del soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'bambino', 'adolescente', 'adulto', 'anziano'."
    ),
    "subjects[].ageRange": (
        "Intervallo di età approssimativo del soggetto in anni. "
        "Campo opzionale/default. "
        "Formato: [min, max], esempio: [25, 30]."
    ),
    "subjects[].genderPresentation": (
        "Presentazione di genere del soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'maschile', 'femminile', 'non binario', 'altro'."
    ),
    "subjects[].ethnicity": (
        "Etnia del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'caucasico', 'asiatico', 'afroamericano', 'latino'."
    ),
    "subjects[].skinTone": (
        "Tono della pelle del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'chiaro', 'medio', 'scuro'."
    ),
    "subjects[].complexion": (
        "Carnagione del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'liscia', 'rugosa', 'macchiata'."
    ),
    "subjects[].hair.color": (
        "Colore dei capelli del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'biondo', 'bruno', 'rosso', 'grigio', 'nero'."
    ),
    "subjects[].hair.length": (
        "Lunghezza dei capelli del soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'corto', 'medio', 'lungo'."
    ),
    "subjects[].hair.style": (
        "Stile dei capelli del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'riccio', 'liscio', 'ondulato', 'rasato'."
    ),
    "subjects[].emotion.primary": (
        "Emozione principale espressa dal soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'felicità', 'tristezza', 'rabbia', 'paura', 'sorpresa', 'disgusto', 'neutro'."
    ),
    "subjects[].emotion.secondary": (
        "Emozione secondaria o sfumatura emotiva. "
        "Campo opzionale/default."
    ),
    "subjects[].pose.body": (
        "Descrizione della posa del corpo del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'in piedi con le braccia incrociate', 'seduto rilassato'."
    ),
    "subjects[].pose.head": (
        "Orientamento della testa del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'rivolto in avanti', 'inclinato a sinistra', 'guardando verso l'alto'."
    ),
    "subjects[].gaze.direction": (
        "Direzione dello sguardo del soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'dritto', 'lontano', 'verso il basso', 'verso l'alto', 'altro'."
    ),
    "subjects[].gaze.intensity": (
        "Intensità dello sguardo. "
        "Campo opzionale/default. "
        "Valori numerici da 0 (debole) a 1 (intenso)."
    ),
    "subjects[].eyeContact": (
        "Indica se il soggetto stabilisce contatto visivo con la fotocamera. "
        "Campo opzionale/default. "
        "Valori booleani: true o false."
    ),
    "subjects[].gestures": (
        "Descrizione di eventuali gesti o movimenti delle mani del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'saluto con la mano', 'mani in tasca'."
    ),
    "subjects[].attire.top": (
        "Descrizione dell'abbigliamento superiore del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'maglietta rossa', 'camicia bianca'."
    ),
    "subjects[].attire.bottom": (
        "Descrizione dell'abbigliamento inferiore del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'jeans blu', 'pantaloni neri'."
    ),
    "subjects[].attire.fullBody": (
        "Descrizione dell'abbigliamento completo, se applicabile. "
        "Campo opzionale/default."
    ),
    "subjects[].accessories": (
        "Accessori indossati dal soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'occhiali da sole', 'cappello', 'collana'."
    ),
    "subjects[].makeup": (
        "Descrizione del trucco del soggetto. "
        "Campo opzionale/default."
    ),
    "subjects[].framing": (
        "Inquadratura del soggetto nell'immagine. "
        "Campo opzionale/default. "
        "Valori ammessi: 'primo piano', 'mezza figura', 'figura intera'."
    ),
    "subjects[].orientations": (
        "Orientamenti del soggetto rispetto alla fotocamera. "
        "Campo opzionale/default. "
        "Esempi: ['frontale', 'laterale', 'retro']. Può essere una lista."
    ),
    "subjects[].anchor": (
        "Punto di ancoraggio del soggetto nell'immagine. "
        "Campo opzionale/default. "
        "Esempi: 'centro', 'basso a sinistra'."
    ),
    "subjects[].scale": (
        "Scala relativa del soggetto nell'immagine. "
        "Campo opzionale/default. "
        "Valori numerici positivi. Esempi: 1.0 (dimensione normale), 0.5 (ridotto)."
    ),
    "subjects[].depthOrder": (
        "Ordine di profondità del soggetto rispetto ad altri elementi. "
        "Campo opzionale/default. "
        "Valori numerici interi, dove 0 è il primo piano."
    ),
    "subjects[].light.sides": (
        "Lati del soggetto illuminati. "
        "Campo opzionale/default. "
        "Esempi: ['fronte', 'sinistra', 'destra', 'retro']."
    ),
    "subjects[].interactionWith": (
        "Descrizione di altre entità con cui il soggetto interagisce. "
        "Campo opzionale/default."
    ),
    "subjects[].interactionType": (
        "Tipo di interazione con altre entità. "
        "Campo opzionale/default. "
        "Esempi: 'contatto fisico', 'sguardo', 'conversazione'."
    ),
    "subjects[].facialExpression.primary": (
        "Espressione facciale primaria del soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'sorridente', 'serio', 'sorpreso', 'arrabbiato', 'neutro'."
    ),
    "subjects[].facialExpression.secondary": (
        "Espressione facciale secondaria o sfumatura. "
        "Campo opzionale/default."
    ),
    "subjects[].microExpressions": (
        "Microespressioni facciali rilevabili. "
        "Campo opzionale/default. "
        "Esempi: 'alzata di sopracciglio', 'stringere le labbra'."
    ),
    "subjects[].movementHint": (
        "Indicazione di movimento o dinamismo del soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'camminando', 'saltando', 'fermo'."
    ),

    "composition": "Sezione dedicata alla composizione visiva dell'immagine.",
    "composition.framingRules": (
        "Regole di inquadratura utilizzate per la composizione. "
        "Campo opzionale/default. "
        "Esempi: ['regola dei terzi', 'regola del triangolo', 'regola della simmetria']."
    ),
    "composition.primarySubject": (
        "Descrizione del soggetto principale nella composizione. "
        "Campo obbligatorio. "
        "Esempi: 'ragazza al centro', 'albero in primo piano'."
    ),
    "composition.secondaryElements": (
        "Elementi secondari presenti nella composizione che supportano il soggetto principale. "
        "Campo opzionale/default. "
        "Esempi: ['nuvole sullo sfondo', 'animali sul lato destro']."
    ),
    "composition.balance": (
        "Descrizione dell'equilibrio visivo nella composizione. "
        "Campo opzionale/default. "
        "Valori ammessi: 'simmetrico', 'asimmetrico', 'radiale'."
    ),
    "composition.visualWeight": (
        "Distribuzione del peso visivo degli elementi nella composizione. "
        "Campo opzionale/default. "
        "Esempi: 'peso maggiore a sinistra', 'bilanciato'."
    ),
    "composition.depthOfField": (
        "Profondità di campo utilizzata nella composizione. "
        "Campo opzionale/default. "
        "Valori ammessi: 'profonda', 'superficiale', 'media'."
    ),
    "composition.bokehQuality": (
        "Qualità del bokeh (sfocatura dello sfondo). "
        "Campo opzionale/default. "
        "Valori ammessi: 'morbido', 'cremoso', 'durezza elevata'."
    ),
    "composition.focusPoint": (
        "Punto di messa a fuoco principale nella composizione. "
        "Campo opzionale/default. "
        "Esempi: 'occhi del soggetto', 'fiore in primo piano'."
    ),
    "composition.leadingLines": (
        "Uso di linee guida nella composizione per guidare lo sguardo. "
        "Campo opzionale/default. "
        "Esempi: 'strada che conduce al soggetto', 'linee del tetto'."
    ),
    "composition.symmetry": (
        "Presenza e tipo di simmetria nella composizione. "
        "Campo opzionale/default. "
        "Valori ammessi: 'simmetria bilaterale', 'simmetria radiale', 'assenza di simmetria'."
    ),
    "composition.geometricShapes": (
        "Forme geometriche evidenti nella composizione. "
        "Campo opzionale/default. "
        "Esempi: ['cerchi', 'triangoli', 'quadrati']."
    ),
    "composition.negativeSpace": (
        "Uso dello spazio negativo nella composizione. "
        "Campo opzionale/default. "
        "Esempi: 'ampio spazio vuoto intorno al soggetto', 'spazio negativo bilanciato'."
    ),
    "composition.cropMargins": (
        "Margini di ritaglio applicati all'immagine. "
        "Campo opzionale/default. "
        "Dizionario con chiavi 'top', 'bottom', 'left', 'right' e valori numerici in percentuale o pixel."
    ),
    "composition.cropMargins.top": (
        "Margine superiore del ritaglio. "
        "Campo opzionale/default. "
        "Valori numerici in percentuale o pixel. Esempi: 5, 10."
    ),
    "composition.cropMargins.bottom": (
        "Margine inferiore del ritaglio. "
        "Campo opzionale/default. "
        "Valori numerici in percentuale o pixel. Esempi: 5, 10."
    ),
    "composition.cropMargins.left": (
        "Margine sinistro del ritaglio. "
        "Campo opzionale/default. "
        "Valori numerici in percentuale o pixel. Esempi: 5, 10."
    ),
    "composition.cropMargins.right": (
        "Margine destro del ritaglio. "
        "Campo opzionale/default. "
        "Valori numerici in percentuale o pixel. Esempi: 5, 10."
    ),
    "composition.aspectRatioConsiderations": (
        "Considerazioni relative all'aspect ratio nella composizione. "
        "Campo opzionale/default. "
        "Esempi: 'mantenere 16:9 per video', 'adattare a 1:1 per social media'."
    ),
    # --- SETTING SECTION ---
    "setting": "Sezione che descrive l'ambiente, il contesto e le condizioni in cui è ambientata l'immagine.",
    "setting.environment": (
        "Descrizione generale dell'ambiente in cui si svolge la scena. "
        "Campo obbligatorio. "
        "Esempi: 'urbano', 'rurale', 'industriale', 'naturale', 'marino', 'montano'."
    ),
    "setting.environmentType": (
        "Tipo specifico di ambiente. "
        "Campo opzionale/default. "
        "Valori ammessi: 'interno', 'esterno'."
    ),
    "setting.timeOfDay": (
        "Momento della giornata in cui è ambientata la scena. "
        "Campo obbligatorio. "
        "Valori ammessi: 'alba', 'mattina', 'mezzogiorno', 'pomeriggio', 'tramonto', 'sera', 'notte'. "
        "Esempi: 'tramonto'."
    ),
    "setting.timeRange": (
        "Intervallo temporale specifico della scena. "
        "Campo opzionale/default. "
        "Formato: ['08:00', '10:30'] (orario 24h)."
    ),
    "setting.weather": (
        "Condizione meteorologica principale della scena. "
        "Campo opzionale/default. "
        "Valori ammessi: 'sereno', 'nuvoloso', 'pioggia', 'neve', 'nebbia', 'vento', 'tempesta', 'foschia', 'variabile'."
    ),
    "setting.weatherDetails": (
        "Dettagli aggiuntivi sulle condizioni meteo. "
        "Campo opzionale/default. "
        "Esempi: 'pioggia leggera', 'cielo parzialmente nuvoloso', 'vento forte da nord'."
    ),
    "setting.temperature": (
        "Temperatura percepita o effettiva nell'ambiente. "
        "Campo opzionale/default. "
        "Valore numerico (°C) o intervallo. Esempi: 22, [-5, 0]."
    ),
    "setting.architecture": (
        "Descrizione generale degli elementi architettonici presenti. "
        "Campo opzionale/default. "
        "Esempi: 'palazzi moderni', 'case in pietra', 'strutture industriali'."
    ),
    "setting.architecturalStyle": (
        "Stile architettonico predominante. "
        "Campo opzionale/default. "
        "Esempi: 'gotico', 'barocco', 'moderno', 'futuristico', 'minimalista'."
    ),
    "setting.cityscape": (
        "Caratteristiche del paesaggio urbano, se applicabile. "
        "Campo opzionale/default. "
        "Esempi: 'skyline con grattacieli', 'piazza affollata', 'quartiere storico'."
    ),
    "setting.foregroundElements": (
        "Elementi rilevanti presenti in primo piano. "
        "Campo opzionale/default. "
        "Esempi: ['fiori', 'panchina', 'cartello stradale']."
    ),
    "setting.middlegroundElements": (
        "Elementi presenti nel piano intermedio della scena. "
        "Campo opzionale/default. "
        "Esempi: ['alberi', 'fontana', 'persone che camminano']."
    ),
    "setting.backgroundElements": (
        "Elementi visibili sullo sfondo della scena. "
        "Campo opzionale/default. "
        "Esempi: ['montagne', 'palazzi', 'cielo nuvoloso']."
    ),
    "setting.season": (
        "Stagione dell'anno rappresentata nella scena. "
        "Campo opzionale/default. "
        "Valori ammessi: 'primavera', 'estate', 'autunno', 'inverno'."
    ),
    "setting.seasonalIndicators": (
        "Indicatori visivi della stagione. "
        "Campo opzionale/default. "
        "Esempi: 'foglie cadute', 'alberi in fiore', 'neve a terra'."
    ),
    "setting.locationHint": (
        "Indicazione di luogo geografico, città o area specifica. "
        "Campo opzionale/default. "
        "Esempi: 'Milano', 'Parigi', 'Alpi svizzere', 'spiaggia tropicale'."
    ),
    "setting.altitude": (
        "Altitudine del luogo rispetto al livello del mare. "
        "Campo opzionale/default. "
        "Valore numerico in metri. Esempi: 1500."
    ),
    "setting.viewDirection": (
        "Direzione di osservazione della scena rispetto ai punti cardinali. "
        "Campo opzionale/default. "
        "Esempi: 'verso nord', 'orientato a sud-ovest'."
    ),
    "setting.ambientSounds": (
        "Suoni ambientali percepibili nella scena (per immagini con componente narrativa o immersiva). "
        "Campo opzionale/default. "
        "Esempi: ['canto degli uccelli', 'rumore del traffico', 'vento tra gli alberi']."
    ),
    "setting.airQuality": (
        "Qualità dell'aria nell'ambiente rappresentato. "
        "Campo opzionale/default. "
        "Valori ammessi: 'ottima', 'buona', 'moderata', 'scarsa', 'inquinata'."
    ),
    "setting.contextualElements": (
        "Elementi contestuali che arricchiscono la scena, suddivisi in marcatori culturali, temporali e sociali. "
        "Campo opzionale/default. "
        "Oggetto con chiavi: 'culturalMarkers', 'timeMarkers', 'socialMarkers'."
    ),
    "setting.contextualElements.culturalMarkers": (
        "Marcatori culturali visibili nella scena, come simboli, bandiere, scritte, architetture tipiche. "
        "Campo opzionale/default. "
        "Esempi: ['bandiera italiana', 'scritta in giapponese', 'mosaico romano']."
    ),
    "setting.contextualElements.timeMarkers": (
        "Elementi che suggeriscono un'epoca storica o un periodo temporale. "
        "Campo opzionale/default. "
        "Esempi: ['automobili anni 60', 'abbigliamento medievale', 'tecnologia futuristica']."
    ),
    "setting.contextualElements.socialMarkers": (
        "Indicatori di status sociale, eventi pubblici o dinamiche sociali nella scena. "
        "Campo opzionale/default. "
        "Esempi: ['manifestazione', 'corteo nuziale', 'raduno giovanile']."
    ),
    # --- LIGHTING SECTION ---
    "lighting": (
        "Sezione che descrive le condizioni di illuminazione della scena e le fonti luminose principali e secondarie. "
        "Fornisce dettagli su direzione, qualità, colore, intensità e altri effetti della luce."
    ),
    "lighting.lightingSetup": (
        "Descrizione generale dello schema di illuminazione adottato nella scena. "
        "Campo opzionale/default. "
        "Esempi: 'Rembrandt', 'farfalla', 'luce a tre punti', 'luce naturale diffusa', 'contrasto alto'."
    ),
    "lighting.primarySources": (
        "Elenco delle fonti luminose principali presenti nella scena. "
        "Campo obbligatorio se si desidera un controllo dettagliato della luce. "
        "Ogni elemento descrive una sorgente luminosa con attributi specifici."
    ),
    "lighting.primarySources[].sourceId": (
        "Identificatore univoco della sorgente luminosa nella scena. "
        "Campo obbligatorio. "
        "Esempi: 'key1', 'fill1', 'sun', 'windowA'."
    ),
    "lighting.primarySources[].type": (
        "Tipologia della sorgente luminosa. "
        "Campo obbligatorio. "
        "Valori ammessi: 'naturale', 'artificiale', 'mista'. "
        "Esempi: 'naturale' per il sole, 'artificiale' per una lampada da studio."
    ),
    "lighting.primarySources[].source": (
        "Origine specifica della luce. "
        "Campo obbligatorio. "
        "Esempi: 'sole', 'lampada LED', 'flash', 'finestra', 'candela', 'insegna al neon'."
    ),
    "lighting.primarySources[].direction": (
        "Direzione da cui proviene la luce rispetto alla scena o al soggetto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'frontale', 'posteriore', 'laterale sinistra', 'laterale destra', 'dall'alto', 'dal basso', 'diagonale', 'contro'."
    ),
    "lighting.primarySources[].angle": (
        "Angolo di incidenza della luce rispetto al soggetto o al piano dell'immagine, espresso in gradi. "
        "Campo opzionale/default. "
        "Valori numerici da 0 a 180. "
        "Esempi: 45 (luce a 45° rispetto al soggetto), 90 (laterale pura)."
    ),
    "lighting.primarySources[].intensity": (
        "Intensità della luce espressa in modo qualitativo. "
        "Campo opzionale/default. "
        "Valori ammessi: 'debole', 'media', 'forte', 'molto forte'."
    ),
    "lighting.primarySources[].intensityValue": (
        "Intensità della luce espressa in valore numerico (ad esempio lux, watt o percentuale). "
        "Campo opzionale/default. "
        "Valori numerici positivi. "
        "Esempi: 1000 (lux), 60 (watt), 0.8 (scala 0-1), 80 (percentuale)."
    ),
    "lighting.primarySources[].colorTemperature": (
        "Temperatura colore della luce espressa in Kelvin (K). "
        "Campo opzionale/default. "
        "Valori numerici tipici: 2000 (luce molto calda), 3200 (tungsteno), 5600 (luce diurna), 6500 (neutra)."
    ),
    "lighting.primarySources[].colorTemperatureDesc": (
        "Descrizione qualitativa della temperatura colore. "
        "Campo opzionale/default. "
        "Valori ammessi: 'calda', 'neutra', 'fredda', 'blu', 'rossastra', 'gialla'."
    ),
    "lighting.primarySources[].quality": (
        "Qualità della luce in termini di diffusione e carattere. "
        "Campo opzionale/default. "
        "Valori ammessi: 'dura', 'morbida', 'diffusa', 'diretta', 'riflessa'."
    ),
    "lighting.primarySources[].qualityDetails": (
        "Dettagli aggiuntivi sulla qualità della luce, ad esempio presenza di filtri, diffusori o riflettori. "
        "Campo opzionale/default. "
        "Esempi: 'luce ammorbidita da softbox', 'riflessa su pannello bianco', 'luce filtrata da tende'."
    ),
    "lighting.primarySources[].hardness": (
        "Grado di durezza della luce su scala numerica da 0 (molto morbida) a 1 (molto dura). "
        "Campo opzionale/default. "
        "Esempi: 0.2 (softbox), 0.8 (flash diretto)."
    ),
    "lighting.primarySources[].shadowType": (
        "Tipologia di ombre prodotte dalla sorgente. "
        "Campo opzionale/default. "
        "Valori ammessi: 'morbide', 'dure', 'sfumate', 'multiple', 'nessuna'."
    ),
    "lighting.primarySources[].effects": (
        "Effetti luminosi particolari generati dalla sorgente. "
        "Campo opzionale/default. "
        "Esempi: ['flare', 'controluce', 'riflesso', 'spot', 'pattern', 'arcobaleno']. "
        "Può essere una lista."
    ),
    "lighting.primarySources[].role": (
        "Ruolo della sorgente luminosa nella scena. "
        "Campo opzionale/default. "
        "Valori ammessi: 'key' (principale), 'fill' (di riempimento), 'back' (controluce), 'rim', 'accent', 'ambient', 'pratica'."
    ),
    "lighting.primarySources[].coverage": (
        "Area o porzione della scena illuminata dalla sorgente. "
        "Campo opzionale/default. "
        "Esempi: 'solo il soggetto', 'sfondo', 'tutta la scena', 'bordo destro'."
    ),
    # --- LIGHTING: FILL LIGHT ---
    "lighting.fillLight": (
        "Descrizione della luce di riempimento utilizzata nella scena. "
        "Campo opzionale/default. "
        "Contiene dettagli su tipo, sorgente, intensità, direzione e colore della fill light."
    ),
    "lighting.fillLight.type": (
        "Tipologia della luce di riempimento. "
        "Campo opzionale/default. "
        "Valori ammessi: 'naturale', 'artificiale', 'riflessa', 'diffusa'. "
        "Esempi: 'artificiale' per una lampada LED, 'riflessa' per un pannello bianco."
    ),
    "lighting.fillLight.source": (
        "Origine specifica della luce di riempimento. "
        "Campo opzionale/default. "
        "Esempi: 'riflettore', 'pannello', 'finestra laterale', 'parete bianca'."
    ),
    "lighting.fillLight.intensity": (
        "Intensità della fill light espressa in modo qualitativo. "
        "Campo opzionale/default. "
        "Valori ammessi: 'debole', 'media', 'forte'."
    ),
    "lighting.fillLight.direction": (
        "Direzione da cui proviene la fill light rispetto al soggetto/scena. "
        "Campo opzionale/default. "
        "Valori ammessi: 'frontale', 'laterale', 'dal basso', 'dall'alto', 'riflessa'."
    ),
    "lighting.fillLight.color": (
        "Colore della luce di riempimento, espresso come descrizione o valore RGB/HEX. "
        "Campo opzionale/default. "
        "Esempi: 'bianco neutro', '#FFD700', 'blu freddo'."
    ),

    # --- LIGHTING: AMBIENT LIGHT ---
    "lighting.ambientLight": (
        "Descrizione della luce ambientale presente nella scena. "
        "Campo opzionale/default. "
        "Contiene dettagli su intensità, sorgente e colore della luce ambientale."
    ),
    "lighting.ambientLight.intensity": (
        "Intensità della luce ambientale. "
        "Campo opzionale/default. "
        "Valori ammessi: 'bassa', 'media', 'alta'."
    ),
    "lighting.ambientLight.source": (
        "Origine della luce ambientale. "
        "Campo opzionale/default. "
        "Esempi: 'luce diffusa dal cielo', 'riflessa dalle pareti', 'illuminazione generale'."
    ),
    "lighting.ambientLight.color": (
        "Colore della luce ambientale. "
        "Campo opzionale/default. "
        "Esempi: 'azzurro freddo', 'giallo caldo', '#AABBCC'."
    ),

    # --- LIGHTING: OVERALL MOOD ---
    "lighting.overallMood": (
        "Descrizione qualitativa dell'atmosfera luminosa generale della scena. "
        "Campo opzionale/default. "
        "Esempi: 'drammatico', 'soft', 'cinematografico', 'neutro', 'misterioso', 'gioioso'."
    ),

    # --- LIGHTING: LIGHTING RATIO ---
    "lighting.lightingRatio": (
        "Rapporto tra la luce principale (key) e la luce di riempimento (fill). "
        "Campo opzionale/default. "
        "Formato: stringa tipo '4:1', '2:1', oppure descrizione qualitativa ('alto contrasto', 'basso contrasto'). "
        "Esempi: '4:1' (key quattro volte più intensa della fill), 'basso contrasto'."
    ),

    # --- LIGHTING: MOOD LINK ---
    "lighting.moodLink": (
        "Collegamento esplicito tra lo schema di illuminazione e l'umore/emozione della scena. "
        "Campo opzionale/default. "
        "Esempi: 'luce dura per enfatizzare tensione', 'illuminazione morbida per atmosfera romantica'."
    ),

    # --- LIGHTING: SHADOW DETAILS ---
    "lighting.shadowDetails": (
        "Dettagli sulle ombre presenti nella scena. "
        "Campo opzionale/default. "
        "Contiene informazioni su densità, bordi e direzione delle ombre."
    ),
    "lighting.shadowDetails.density": (
        "Densità/opacità delle ombre. "
        "Campo opzionale/default. "
        "Valori ammessi: 'leggere', 'medie', 'dense', oppure valore numerico da 0 (trasparente) a 1 (opaca)."
    ),
    "lighting.shadowDetails.edges": (
        "Carattere dei bordi delle ombre. "
        "Campo opzionale/default. "
        "Valori ammessi: 'nitidi', 'sfumati', 'misti'."
    ),
    "lighting.shadowDetails.direction": (
        "Direzione prevalente delle ombre rispetto alla scena o al soggetto. "
        "Campo opzionale/default. "
        "Esempi: 'da sinistra a destra', 'verso il basso', 'retroilluminazione'."
    ),

    # --- LIGHTING: HIGHLIGHTS ---
    "lighting.highlights": (
        "Informazioni sui punti di massima luminosità (highlights) nell'immagine. "
        "Campo opzionale/default. "
        "Contiene dettagli su preservazione, rolloff e clipping delle alte luci."
    ),
    "lighting.highlights.preservation": (
        "Livello di preservazione dei dettagli nelle alte luci. "
        "Campo opzionale/default. "
        "Valori ammessi: 'alta', 'media', 'bassa'."
    ),
    "lighting.highlights.rolloff": (
        "Gradualità di transizione tra aree luminose e ombre (rolloff). "
        "Campo opzionale/default. "
        "Valori ammessi: 'dolce', 'rapida', 'lineare'."
    ),
    "lighting.highlights.clipping": (
        "Presenza o assenza di clipping nelle alte luci (perdita di dettaglio). "
        "Campo opzionale/default. "
        "Valori ammessi: 'nessun clipping', 'clipping lieve', 'clipping marcato'."
    ),

    # --- LIGHTING: CHALLENGES ---
    "lighting.lightingChallenges": (
        "Eventuali difficoltà o problematiche legate all'illuminazione della scena. "
        "Campo opzionale/default. "
        "Esempi: 'alto contrasto difficile da gestire', 'riflessi indesiderati', 'zone in ombra non controllabili'."
    ),

    # --- LIGHTING: POST-PROCESSING HINTS ---
    "lighting.postProcessingHints": (
        "Suggerimenti relativi alla post-produzione per la gestione della luce. "
        "Campo opzionale/default. "
        "Esempi: 'recuperare dettagli nelle ombre', 'attenuare le alte luci', 'aumentare il contrasto locale', 'applicare split toning'."
    ),
    # --- STYLE SECTION ---
    "style": (
        "Sezione dedicata allo stile visivo, artistico e all'atmosfera dell'immagine. "
        "Comprende scelte di direzione artistica, mood, tendenze estetiche e trattamenti cromatici o testurali."
    ),
    "style.artDirection": (
        "Direzione artistica generale dell'immagine, che orienta l'approccio stilistico e visivo. "
        "Campo opzionale/default. "
        "Esempi: 'minimalista', 'surreale', 'realismo magico', 'pittorico', 'cinematografico', 'editoriale', 'fashion', 'fine art'."
    ),
    "style.photographyStyle": (
        "Stile fotografico di riferimento per l'immagine. "
        "Campo opzionale/default. "
        "Valori ammessi: 'documentaristico', 'ritratto', 'street', 'paesaggio', 'macro', 'still life', 'fashion', 'concettuale', 'reportage', 'architettura', 'editoriale'. "
        "Esempi: 'ritratto', 'street'."
    ),
    "style.mood": (
        "Umore o atmosfera emotiva che si desidera trasmettere con l'immagine. "
        "Campo obbligatorio. "
        "Esempi: 'melanconico', 'gioioso', 'misterioso', 'drammatico', 'sereno', 'dinamico', 'intenso', 'rilassato'."
    ),
    "style.moodIntensity": (
        "Intensità dell'umore o atmosfera espressa. "
        "Campo opzionale/default. "
        "Valori numerici da 0 (molto lieve) a 1 (massima intensità), oppure descrittori: 'lieve', 'moderato', 'forte'. "
        "Esempi: 0.8, 'forte'."
    ),
    "style.aestheticInfluences": (
        "Influenze estetiche, movimenti artistici o correnti che ispirano lo stile dell'immagine. "
        "Campo opzionale/default. "
        "Esempi: ['impressionismo', 'barocco', 'pop art', 'vaporwave', 'futurismo', 'bauhaus', 'art déco', 'surrealismo']."
    ),
    "style.contrastLevel": (
        "Livello di contrasto percepito nell'immagine. "
        "Campo opzionale/default. "
        "Valori ammessi: 'basso', 'medio', 'alto', 'estremo'."
    ),
    "style.contrastValue": (
        "Valore numerico di contrasto, per un controllo più preciso. "
        "Campo opzionale/default. "
        "Valori numerici da 0 (nessun contrasto) a 1 (massimo contrasto). "
        "Esempi: 0.3, 0.85."
    ),
    "style.colorTone": (
        "Tonalità cromatica dominante dell'immagine. "
        "Campo opzionale/default. "
        "Esempi: 'caldo', 'freddo', 'neutro', 'seppia', 'monocromatico', 'pastello', 'vivace', 'desaturato'."
    ),
    "style.colorTemperature": (
        "Temperatura colore dominante. "
        "Campo opzionale/default. "
        "Valori numerici in Kelvin (K) o descrittori: 'calda', 'fredda', 'neutra'. "
        "Esempi: 3200, 6500, 'calda'."
    ),
    "style.texture": (
        "Carattere generale della texture visiva dell'immagine. "
        "Campo opzionale/default. "
        "Esempi: 'liscia', 'materica', 'grana accentuata', 'vellutata', 'ruvida', 'pittorica', 'patinata'."
    ),
    "style.textureDetails": (
        "Dettagli specifici sulle texture presenti o desiderate. "
        "Campo opzionale/default. "
        "Esempi: 'grana fine tipo pellicola', 'pennellate visibili', 'effetto carta', 'disturbo digitale', 'patina vintage'."
    ),
    "style.dynamicRange": (
        "Gamma dinamica percepita o desiderata nell'immagine. "
        "Campo opzionale/default. "
        "Valori ammessi: 'bassa', 'media', 'alta', oppure valore numerico (es. 12, 14 stop)."
    ),
    "style.postProcessingStyle": (
        "Stile di post-produzione o trattamento digitale previsto. "
        "Campo opzionale/default. "
        "Esempi: 'contrasto elevato', 'color grading teal and orange', 'split toning', 'desaturazione selettiva', 'effetto HDR', 'filtro analogico', 'soft focus', 'vignettatura'."
    ),
    "style.filmEmulation": (
        "Indicazione di emulazione di pellicola fotografica specifica. "
        "Campo opzionale/default. "
        "Esempi: 'Kodak Portra 400', 'Fujifilm Velvia', 'Ilford HP5', 'Polaroid', 'Kodachrome'."
    ),
    "style.vintageEffect": (
        "Effetti vintage, retrò o di invecchiamento applicati all'immagine. "
        "Campo opzionale/default. "
        "Esempi: 'colori sbiaditi', 'cornice Polaroid', 'effetto pellicola graffiata', 'viraggio seppia', 'luce diffusa anni 70'."
    ),
    "style.references": (
        "Riferimenti visivi o artistici espliciti, come immagini di esempio, opere d'arte, fotografi o registi. "
        "Campo opzionale/default. "
        "Esempi: ['fotografie di Annie Leibovitz', 'film di Wes Anderson', 'pittura di Monet', 'campagna Gucci 2022']."
    ),
    "style.inspirationKeywords": (
        "Parole chiave ispirazionali che guidano lo stile o l'atmosfera dell'immagine. "
        "Campo opzionale/default. "
        "Esempi: ['onirico', 'cinematografico', 'urban', 'futuristico', 'noir', 'romantico', 'high fashion']."
    ),
    "style.avoidKeywords": (
        "Parole chiave o concetti da evitare esplicitamente nello stile o nella resa finale. "
        "Campo opzionale/default. "
        "Esempi: ['cartoon', 'eccesso di saturazione', 'HDR estremo', 'effetto plastica', 'low poly']."
    ),

    # --- RENDERING SECTION ---
    "rendering": (
        "Sezione che descrive i parametri tecnici e qualitativi della resa finale dell'immagine e le modalità di esportazione. "
        "Comprende la scelta del motore di rendering, preset visivi, profili di color grading, risoluzione, formati di esportazione e impostazioni specifiche per engine AI."
    ),
    # --- ENGINE FIELDS ---
    "rendering.engine": (
        "Motore principale utilizzato per la generazione/rendering dell'immagine. "
        "Campo di sistema/default (preimpostato in base alla piattaforma o alle preferenze). "
        "Valori ammessi: 'midjourney', 'dalle', 'stablediffusion', 'gpt4', 'sora', ecc. "
        "Esempio: 'midjourney'."
    ),
    "rendering.primaryEngine": (
        "Motore AI primario selezionato per la generazione dell'immagine. "
        "Campo di sistema/default. "
        "Valori come per 'rendering.engine'. "
        "Esempio: 'stablediffusion'."
    ),
    "rendering.fallbackEngines": (
        "Lista di motori AI alternativi da utilizzare in caso di errore del motore principale. "
        "Campo di sistema/default. "
        "Esempio: ['dalle', 'midjourney']."
    ),
    "rendering.engineSpecificSettings": (
        "Oggetto che contiene impostazioni avanzate specifiche per ciascun motore di rendering AI. "
        "Campo di sistema/default. "
        "Chiavi tipiche: 'midjourney', 'dalle', 'stablediffusion', 'gpt4', 'sora'."
    ),
    "rendering.engineSpecificSettings.midjourney": (
        "Impostazioni avanzate specifiche per il motore Midjourney. "
        "Campo di sistema/default. "
        "Esempio: {'version': 'v5.2', 'style': 'raw', 'quality': 2}."
    ),
    "rendering.engineSpecificSettings.dalle": (
        "Impostazioni avanzate specifiche per il motore DALL·E. "
        "Campo di sistema/default. "
        "Esempio: {'model': 'dalle-3', 'style': 'vivid'}."
    ),
    "rendering.engineSpecificSettings.stablediffusion": (
        "Impostazioni avanzate per Stable Diffusion (es. scheduler, steps, guidance scale). "
        "Campo di sistema/default. "
        "Esempio: {'steps': 30, 'guidance_scale': 7.5, 'sampler': 'Euler a'}."
    ),
    "rendering.engineSpecificSettings.gpt4": (
        "Impostazioni specifiche per la generazione visuale tramite GPT-4 o modelli multimodali correlati. "
        "Campo di sistema/default. "
        "Esempio: {'vision_mode': 'high', 'temperature': 0.7}."
    ),
    "rendering.engineSpecificSettings.sora": (
        "Impostazioni specifiche per il motore Sora (es. frame rate, durata video). "
        "Campo di sistema/default. "
        "Esempio: {'frame_rate': 24, 'duration': 10}."
    ),
    # --- USER-EDITABLE FIELDS ---
    "rendering.lookPreset": (
        "Preset visivo globale che definisce l'aspetto generale dell'immagine. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'realistico', 'cinematografico', 'pittorico', 'cartoon', 'stilizzato', ecc. "
        "Esempi: 'realistico', 'teal and orange', 'bianco e nero'."
    ),
    "rendering.colorGradingProfile": (
        "Profilo di color grading applicato all'immagine. "
        "Campo modificabile dall'utente. "
        "Esempi: 'Kodak', 'Fuji', 'cinema warm', 'look vintage', 'neutral'."
    ),
    "rendering.colorGradingIntensity": (
        "Intensità dell'effetto di color grading. "
        "Campo modificabile dall'utente. "
        "Valori numerici da 0 (nessun effetto) a 1 (massima intensità). "
        "Esempi: 0.5, 1.0."
    ),
    "rendering.exportFormats": (
        "Lista dei formati di esportazione desiderati per l'immagine finale. "
        "Campo modificabile dall'utente. "
        "Valori ammessi: 'jpg', 'png', 'tiff', 'webp', 'bmp', ecc. "
        "Esempi: ['jpg', 'png']."
    ),
    "rendering.resolutionTarget": (
        "Target di risoluzione desiderato espresso come stringa o oggetto. "
        "Campo modificabile dall'utente. "
        "Formati accettati: '4K', '8K', '1080p', oppure oggetto {'width': 1920, 'height': 1080}. "
        "Esempi: '4K', {'width': 2048, 'height': 2048}."
    ),
    "rendering.iterations": (
        "Numero di iterazioni o versioni da generare (utile per batch o selezione del miglior risultato). "
        "Campo modificabile dall'utente. "
        "Valori numerici interi >= 1. "
        "Esempio: 4."
    ),
    # --- SYSTEM/DEFAULT FIELDS ---
    "rendering.fidelitySpec": (
        "Specifica tecnica del livello di fedeltà della generazione. "
        "Campo di sistema/default. "
        "Oggetto con chiavi come 'detail', 'photorealism', 'noiseLevel', 'sharpness'."
    ),
    "rendering.fidelitySpec.detail": (
        "Livello di dettaglio desiderato nella resa. "
        "Campo di sistema/default. "
        "Valori ammessi: 'basso', 'medio', 'alto', 'estremo', oppure valore numerico (es. 0.8)."
    ),
    "rendering.fidelitySpec.photorealism": (
        "Grado di fotorealismo richiesto. "
        "Campo di sistema/default. "
        "Valori ammessi: 'nessuno', 'medio', 'alto', 'estremo', oppure valore numerico (es. 1.0)."
    ),
    "rendering.fidelitySpec.noiseLevel": (
        "Livello di rumore/grana nella resa finale. "
        "Campo di sistema/default. "
        "Valori ammessi: 'basso', 'medio', 'alto', oppure valore numerico (es. 0.2)."
    ),
    "rendering.fidelitySpec.sharpness": (
        "Grado di nitidezza applicato all'immagine. "
        "Campo di sistema/default. "
        "Valori numerici da 0 a 1, oppure 'soft', 'sharp', 'extra-sharp'."
    ),
    "rendering.resolutionPx": (
        "Risoluzione finale in pixel dell'immagine generata. "
        "Campo di sistema/default. "
        "Oggetto {'width': int, 'height': int}. "
        "Esempio: {'width': 4096, 'height': 4096}."
    ),
    "rendering.compressionQuality": (
        "Qualità di compressione applicata durante l'esportazione (tipicamente per JPG/WebP). "
        "Campo di sistema/default. "
        "Valori numerici da 0 (bassa qualità, alta compressione) a 1 (massima qualità). "
        "Esempio: 0.92."
    ),
    "rendering.bitDepth": (
        "Profondità di colore dell'immagine esportata, in bit per canale. "
        "Campo di sistema/default. "
        "Valori tipici: 8, 10, 16."
    ),
    "rendering.renderTime": (
        "Tempo impiegato per la generazione/rendering dell'immagine, espresso in secondi. "
        "Campo di sistema/default. "
        "Esempio: 12.4."
    ),
    "rendering.upscalingMethod": (
        "Metodo di upscaling applicato per aumentare la risoluzione. "
        "Campo di sistema/default. "
        "Valori ammessi: 'none', 'ESRGAN', 'RealESRGAN', 'Lanczos', 'AI', ecc. "
        "Esempio: 'RealESRGAN'."
    ),
    "rendering.qualityAssurance": (
        "Risultato o stato della verifica automatica della qualità dell'immagine generata. "
        "Campo di sistema/default. "
        "Esempi: 'passed', 'flagged', 'needs review', 'failed'."
    ),
    # --- COLOR PLATE SECTION ---
    "colorPlate": (
        "Sezione che raccoglie tutte le informazioni cromatiche principali dell'immagine. "
        "Include palette, armonia, accessibilità, stagionalità e considerazioni culturali. "
        "Campo opzionale/default."
    ),
    "colorPlate.colorScheme": (
        "Schema colore dominante dell'immagine. "
        "Campo opzionale/default. "
        "Valori ammessi: 'monocromatico', 'complementare', 'analoghi', 'triadico', 'tetradico', 'split-complementary', ecc. "
        "Esempi: 'complementare', 'analoghi'."
    ),
    "colorPlate.primaryColors": (
        "Lista dei colori principali utilizzati nell'immagine, ordinati per importanza o presenza. "
        "Campo opzionale/default. "
        "Ogni elemento è un oggetto con dettagli sul colore."
    ),
    "colorPlate.primaryColors[].name": (
        "Nome descrittivo del colore principale. "
        "Campo opzionale/default. "
        "Esempi: 'blu oltremare', 'giallo ocra', 'rosso rubino'."
    ),
    "colorPlate.primaryColors[].hex": (
        "Codice colore in formato HEX. "
        "Campo opzionale/default. "
        "Esempi: '#FF5733', '#0044CC'."
    ),
    "colorPlate.primaryColors[].rgb": (
        "Valore RGB del colore principale. "
        "Campo opzionale/default. "
        "Formato: [R, G, B], esempio: [255, 87, 51]."
    ),
    "colorPlate.primaryColors[].percentage": (
        "Percentuale stimata di presenza del colore nell'immagine (0-100). "
        "Campo opzionale/default. "
        "Esempi: 45, 12."
    ),
    "colorPlate.primaryColors[].role": (
        "Ruolo del colore nella scena. "
        "Campo opzionale/default. "
        "Valori ammessi: 'dominante', 'di supporto', 'sfondo', 'accento'."
    ),
    "colorPlate.primaryColors[].lightingInteraction": (
        "Descrizione di come il colore interagisce con la luce. "
        "Campo opzionale/default. "
        "Esempi: 'riflette la luce', 'assorbe ombre', 'cambia tonalità alla luce calda'."
    ),
    "colorPlate.accentColors": (
        "Lista dei colori di accento utilizzati per dettagli o punti focali. "
        "Campo opzionale/default. "
        "Struttura analoga a 'primaryColors'."
    ),
    "colorPlate.accentColors[].name": (
        "Nome descrittivo del colore di accento. "
        "Campo opzionale/default. "
        "Esempi: 'verde lime', 'arancione acceso'."
    ),
    "colorPlate.accentColors[].hex": (
        "Codice colore in formato HEX per il colore di accento. "
        "Campo opzionale/default. "
        "Esempi: '#00FF00', '#FFA500'."
    ),
    "colorPlate.accentColors[].rgb": (
        "Valore RGB del colore di accento. "
        "Campo opzionale/default. "
        "Formato: [R, G, B]."
    ),
    "colorPlate.accentColors[].percentage": (
        "Percentuale stimata di presenza del colore di accento. "
        "Campo opzionale/default. "
        "Esempi: 5, 8."
    ),
    "colorPlate.accentColors[].role": (
        "Ruolo del colore di accento. "
        "Campo opzionale/default. "
        "Valori ammessi: 'accento', 'dettaglio', 'contrasto'."
    ),
    "colorPlate.accentColors[].lightingInteraction": (
        "Descrizione di come il colore di accento interagisce con la luce. "
        "Campo opzionale/default. "
        "Esempi: 'accentua i riflessi', 'brilla sotto la luce artificiale'."
    ),
    "colorPlate.colorHarmony": (
        "Tipo di armonia cromatica utilizzata. "
        "Campo opzionale/default. "
        "Valori ammessi: 'armoniosa', 'contrastata', 'bilanciata', 'azzardata'."
    ),
    "colorPlate.colorTemperature": (
        "Temperatura colore generale della palette. "
        "Campo opzionale/default. "
        "Valori numerici (Kelvin) o descrittori: 'calda', 'fredda', 'neutra'. "
        "Esempi: 6500, 'calda'."
    ),
    "colorPlate.saturationLevel": (
        "Livello di saturazione complessiva della palette. "
        "Campo opzionale/default. "
        "Valori ammessi: 'bassa', 'media', 'alta', oppure valore numerico (es. 0.7)."
    ),
    "colorPlate.saturationValue": (
        "Valore numerico di saturazione media (0-1). "
        "Campo opzionale/default. "
        "Esempi: 0.3, 0.85."
    ),
    "colorPlate.contrastWithLighting": (
        "Descrizione del contrasto cromatico in relazione alla luce presente. "
        "Campo opzionale/default. "
        "Esempi: 'alto contrasto con luce dura', 'basso contrasto in luce diffusa'."
    ),
    "colorPlate.dominantColor": (
        "Colore dominante assoluto nell'immagine. "
        "Campo opzionale/default. "
        "Esempi: 'blu navy', '#112244', [17, 34, 68]."
    ),
    "colorPlate.colorMoodAlignment": (
        "Allineamento tra la palette cromatica e il mood/emozione della scena. "
        "Campo opzionale/default. "
        "Esempi: 'colori freddi per trasmettere calma', 'toni caldi per atmosfera accogliente'."
    ),
    "colorPlate.colorAccessibility": (
        "Considerazioni di accessibilità cromatica (es. compatibilità con daltonismo). "
        "Campo opzionale/default. "
        "Esempi: 'palette accessibile a deuteranopia', 'alto contrasto per leggibilità'."
    ),
    "colorPlate.seasonalAppropriate": (
        "Adeguatezza della palette rispetto alla stagione rappresentata. "
        "Campo opzionale/default. "
        "Esempi: 'toni autunnali', 'palette primaverile', 'colori invernali freddi'."
    ),
    "colorPlate.culturalConsiderations": (
        "Considerazioni culturali legate all'uso dei colori (significati, simbolismi, tabù). "
        "Campo opzionale/default. "
        "Esempi: 'evitare rosso per contesto funebre', 'utilizzo di oro per festività asiatica'."
    ),

    # --- QUALITY SECTION ---
    "quality": (
        "Sezione che raccoglie i requisiti tecnici, estetici e le eventuali restrizioni o vincoli di qualità richiesti per l'immagine. "
        "Campo opzionale/default."
    ),
    "quality.technicalRequirements": (
        "Requisiti tecnici minimi o desiderati per la generazione/rendering dell'immagine. "
        "Campo opzionale/default. "
        "Oggetto con sotto-campi specifici."
    ),
    "quality.technicalRequirements.resolution": (
        "Risoluzione minima o raccomandata per l'immagine. "
        "Campo opzionale/default. "
        "Esempi: '4K', {'width': 3840, 'height': 2160}."
    ),
    "quality.technicalRequirements.dpi": (
        "DPI (dots per inch) richiesto per l'immagine finale. "
        "Campo opzionale/default. "
        "Esempi: 300."
    ),
    "quality.technicalRequirements.colorDepth": (
        "Profondità di colore minima richiesta (bit per canale). "
        "Campo opzionale/default. "
        "Esempi: 8, 10, 16."
    ),
    "quality.technicalRequirements.noiseLevel": (
        "Livello massimo di rumore/grana accettato. "
        "Campo opzionale/default. "
        "Valori ammessi: 'basso', 'medio', 'alto', oppure valore numerico (es. 0.2)."
    ),
    "quality.technicalRequirements.compression": (
        "Livello di compressione massimo accettato o formato. "
        "Campo opzionale/default. "
        "Esempi: 'nessuna compressione', 'JPEG qualità > 90%'."
    ),
    "quality.technicalRequirements.fileFormat": (
        "Formato file richiesto. "
        "Campo opzionale/default. "
        "Esempi: 'PNG', 'TIFF', 'JPEG'."
    ),
    "quality.technicalRequirements.colorProfile": (
        "Profilo colore richiesto (es. sRGB, AdobeRGB). "
        "Campo opzionale/default. "
        "Esempi: 'sRGB'."
    ),
    "quality.technicalRequirements.aspectRatio": (
        "Rapporto d'aspetto minimo o richiesto. "
        "Campo opzionale/default. "
        "Esempi: '16:9', '1:1'."
    ),
    "quality.technicalRequirements.fidelity": (
        "Livello di fedeltà tecnica richiesto. "
        "Campo opzionale/default. "
        "Valori ammessi: 'alta', 'media', 'bassa'."
    ),
    "quality.aestheticRequirements": (
        "Requisiti estetici o stilistici da rispettare nella resa dell'immagine. "
        "Campo opzionale/default. "
        "Oggetto con sotto-campi."
    ),
    "quality.aestheticRequirements.consistency": (
        "Richiesta di coerenza visiva (es. tra più immagini o rispetto a uno stile di riferimento). "
        "Campo opzionale/default. "
        "Esempi: 'coerenza con set precedente', 'uniformità cromatica'."
    ),
    "quality.aestheticRequirements.moodAdherence": (
        "Aderenza all'umore/mood richiesto. "
        "Campo opzionale/default. "
        "Esempi: 'mantenere mood malinconico', 'evitare toni troppo accesi'."
    ),
    "quality.aestheticRequirements.subjectClarity": (
        "Chiarezza nella resa del soggetto principale. "
        "Campo opzionale/default. "
        "Esempi: 'soggetto sempre a fuoco', 'volto ben leggibile'."
    ),
    "quality.aestheticRequirements.compositionRules": (
        "Rispetto di regole compositive specifiche. "
        "Campo opzionale/default. "
        "Esempi: 'seguire regola dei terzi', 'simmetria centrale'."
    ),
    "quality.aestheticRequirements.colorBalance": (
        "Richiesta di bilanciamento cromatico. "
        "Campo opzionale/default. "
        "Esempi: 'evitare dominanti verdi', 'bilanciamento neutro'."
    ),
    "quality.aestheticRequirements.textureQuality": (
        "Livello di qualità delle texture o dettagli superficiali. "
        "Campo opzionale/default. "
        "Valori ammessi: 'alta', 'media', 'bassa'."
    ),
    "quality.constraintsAndAvoidances": (
        "Vincoli, restrizioni e aspetti da evitare o garantire nella generazione. "
        "Campo opzionale/default. "
        "Oggetto con chiavi 'avoid' e 'ensure'."
    ),
    "quality.constraintsAndAvoidances.avoid": (
        "Elenco di elementi, difetti o caratteristiche da evitare. "
        "Campo opzionale/default. "
        "Esempi: ['artefatti digitali', 'soggetto sfocato', 'colori innaturali']."
    ),
    "quality.constraintsAndAvoidances.ensure": (
        "Elenco di requisiti da garantire. "
        "Campo opzionale/default. "
        "Esempi: ['alta nitidezza', 'contrasto sufficiente', 'palette coerente']."
    ),

    # --- VARIATIONS SECTION ---
    "variations": (
        "Sezione dedicata alle richieste di variazioni o alternative rispetto al prompt principale. "
        "Campo opzionale/default."
    ),
    "variations.alternativeAngles": (
        "Richiesta di varianti con angoli di ripresa alternativi. "
        "Campo opzionale/default. "
        "Esempi: ['vista laterale', 'dall'alto', 'dal basso']."
    ),
    "variations.alternativeExpressions": (
        "Richiesta di varianti con espressioni facciali o emotive differenti. "
        "Campo opzionale/default. "
        "Esempi: ['soggetto sorridente', 'espressione seria', 'sguardo sorpreso']."
    ),
    "variations.alternativeLighting": (
        "Richiesta di varianti con condizioni di illuminazione diverse. "
        "Campo opzionale/default. "
        "Esempi: ['luce calda', 'luce fredda', 'controluce', 'luce soffusa']."
    ),
    "variations.alternativeCompositions": (
        "Richiesta di alternative nella composizione (es. inquadratura, disposizione soggetti). "
        "Campo opzionale/default. "
        "Esempi: ['framing più stretto', 'soggetto decentrato', 'sfondo diverso']."
    ),
    "variations.seedModifications": (
        "Richiesta di variazioni tramite modifiche ai parametri seed/randomizzazione. "
        "Campo opzionale/default. "
        "Oggetto con sotto-campi."
    ),
    "variations.seedModifications.parameter": (
        "Parametro di generazione da variare (tipicamente 'seed'). "
        "Campo opzionale/default. "
        "Esempi: 'seed', 'noise_seed'."
    ),
    "variations.seedModifications.range": (
        "Intervallo di valori per la variazione del parametro. "
        "Campo opzionale/default. "
        "Esempi: [1000, 1005]."
    ),
    "variations.seedModifications.options": (
        "Lista di valori specifici da testare per il parametro. "
        "Campo opzionale/default. "
        "Esempi: [12345, 54321, 67890]."
    ),

    # --- METADATA SECTION ---
    "metadata": (
        "Sezione contenente informazioni tecniche e statistiche avanzate sulla generazione, utilizzo e performance del prompt. "
        "Campo di sistema/non modificabile direttamente dall'utente."
    ),
    "metadata.usage": (
        "Descrizione o nota d'uso del prompt (scopo, contesto di utilizzo). "
        "Campo di sistema/opzionale. "
        "Esempi: 'per campagna social', 'test qualità engine', 'dataset training'."
    ),
    "metadata.compatibleEngines": (
        "Lista di motori AI compatibili con il prompt. "
        "Campo di sistema. "
        "Esempi: ['midjourney', 'stablediffusion', 'dalle']."
    ),
    "metadata.promptComplexity": (
        "Valutazione della complessità del prompt (automatica o dichiarata). "
        "Campo di sistema. "
        "Valori ammessi: 'bassa', 'media', 'alta'."
    ),
    "metadata.estimatedTokens": (
        "Numero stimato di token utilizzati dal prompt (per modelli LLM). "
        "Campo di sistema. "
        "Esempi: 220."
    ),
    "metadata.processingTime": (
        "Tempo di elaborazione stimato o effettivo per la generazione (in secondi). "
        "Campo di sistema. "
        "Esempi: 3.2."
    ),
    "metadata.lastTested": (
        "Data e ora dell'ultimo test del prompt (ISO 8601). "
        "Campo di sistema. "
        "Esempi: '2024-05-01T21:00:00Z'."
    ),
    "metadata.successRate": (
        "Percentuale di generazioni riuscite con questo prompt. "
        "Campo di sistema. "
        "Esempi: 0.97."
    ),
    "metadata.commonIssues": (
        "Problemi comuni riscontrati nell'uso di questo prompt. "
        "Campo di sistema. "
        "Esempi: ['soggetto sfocato', 'colori innaturali', 'errore engine']."
    ),
    "metadata.optimizationNotes": (
        "Note di ottimizzazione o suggerimenti tecnici per migliorare la resa del prompt. "
        "Campo di sistema. "
        "Esempi: 'ridurre lunghezza prompt', 'specificare meglio il soggetto', 'aggiungere dettagli sulla luce'."
    )

}

# Elenco dei campi obbligatori da mostrare sempre all'utente
MANDATORY_FIELDS = [
    # META
    "meta.title",
    "meta.tags",
    "meta.aspectRatio",
    "meta.orientation",
    "meta.colorProfile",
    "meta.dpi",
    "meta.category",

    # SUBJECTS
    "subjects[].descriptor",

    # COMPOSITION
    "composition.primarySubject",

    # SETTING
    "setting.environment",
    "setting.timeOfDay",

    # LIGHTING
    "lighting.primarySources",
    "lighting.primarySources[].sourceId",
    "lighting.primarySources[].type",
    "lighting.primarySources[].source",

    # STYLE
    "style.mood"
]
