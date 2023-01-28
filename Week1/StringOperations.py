weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, with plenty of winter sunshine developing. However, patchy cloud and isolated showers may move in from the west later in the afternoon."

weatherNewLine = weather.split("\n")
weatherSpace = weather.split(" ")
weatherFullStop = weather.split(".")
weatherLC = weather.lower()
weatherSunshine = weather.find("sunshine")

print(weatherNewLine)
print(weatherSpace)
print(weatherFullStop)
print(len(weather))
print(weatherLC)
print(weatherSunshine)