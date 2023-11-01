---
description: Implementation av USB synkroniseringsstrategier för isochronous endpoints
image: /img/hardware/RustSoundCard/developmentHardware.jpg
---

# Ljudkort i Rust

Mitt exjobb gick ut på att implementera funktionalitet för Rusts `usb-device`
crate, för att bygga ett ljudkort. Craten i fråga implementerar en USB stack för
device applikationer, och stöder många olika mikrokontrollers. Det var dock en
bit som fattades i denna implementation. Fallet var att när man satte upp
endpoints för USB, fattades två delar av endpoint descriptorn som krävs för att
använda isochrona endpoints till fullo.


