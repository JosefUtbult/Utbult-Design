---
description: An introduction to build rust code for embedded systems
image: Hardware/img/EmbeddedRust/nRF52840.jpg
---

# Embedded Rust - An introduction

## Vad är Rust?
>Rust is a modern systems programming language developed by the Mozilla Corporation. It is intended to be a language for highly concurrent and highly secure systems. It compiles to native code; hence, it is blazingly fast like C and C++.

[Tutorialspoint on Rust](https://www.tutorialspoint.com/rust/index.htm)

Vad är då fördelen med Rust?
>Systems and application programming languages face two major problems
>-   It is difficult to write secure code.
>-   It is difficult to write multi-threaded code.

Iden med Rust är att ha ett programmeringsspråk som prioriterar att utveckla snabba, hårdvarunära program. Detta görs med _concurrency_, dvs att programmet består av olika delar som kan köras samtidigt.

## Rustup
[Tutorialspoint](https://www.tutorialspoint.com/rust/rust_environment_setup.htm)

_Rustup_ är ett terminalbaserat verktyg för att hantera versioner av rustkompilatorn och de verktyg som krävs för att kompilera rustkod.

När rustup installeras kommer också en kompilator för rust att hänga med, kallad _rustc_.

### Rustup installation - Manjaro
```
sudo pacman -S rustup
```

## Introduktion till rust
Här kommer en introduktion till rust. Om du känner att du har koll kan du skippa den. Annars om du känner dig relativt säker men vill ha en genomgång om ägandeskap kan du kolla [[#Exempel 8 - Ägandeskap]] och [[#Exempel 9 - Lånande]].

### Exempel 1 - Hello World
Vi börjar med ett enkelt exempel. Vi ska skriva ett _hello world_ program i rust och kompilerar det för att köras på din dator.

Börja med att skapa en mapp som heter `exempel1-helloWorld`
```
mkdir exempel1-helloWorld
cd exempel1-helloWorld
```

Där i vill vi skapa sourcefilen för hello world programmet
```
touch helloWorld.rs
```

Notera att filändelsen för rust är `.rs`

Senare går vi igenom hur man använder en IDE för att skriva, kompilera och köra rustkod i. Men för enkelhetens skull börjar vi med att använda en textredigerare för att skriva koden i och en terminal för att kompilera och köra i.

Öppna denna fil i en textredigerare. Jag rekommenderar [Sublime Text](https://www.sublimetext.com/) för enkelhetens skull. Där lägger du till.

```rust
fn main()  
{
	println!("Hello world!");  
}
```
