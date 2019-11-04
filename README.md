# Workshop de Raspberry Pi.
Minha parte de um workshop de Raspberry Pi que fiz enquanto membro do Projeta Planeta 4.0. Fiquei responsável por ensinar o protocolo MQTT.

## Instalação de bibliotecas

É necessário instalar primeiro a biblioteca Eclipse Paho. Siga as instruções no site https://pypi.org/project/paho-mqtt/#installation, são bem simples.

Você vai precisar de seu celular para ver o protocolo em ação. Procure na App Store algum aplicativo que tenha protocolo MQTT. Para celulares Android, recomendo o MQTT Dash. Quando abrir, coloque de endereço "iot.eclipse.org", de nome coloque o que quiser.

Ao conectar, clique no *+*, e selecione Text. Você criará 2 Topics. Name, dê o nome que quiser, mas os Topics deve ser "JezSubscribe" e "JezCursoDeRasp".

Execute o código Python, e escolha uma das 2 alternativas: publicar no celular ou receber no celular. **ATENÇÃO, você não pode alternar entre os dois, tem que ser um até o fim.** Se quiser trocar os dois de função, terá que parar o código e reexecutar e escolher a outra alternativa.

Tentamos fazer isso, mas não é possível. Tiro a conclusão que o protocolo é **half-duplex**: celular e Rasp podem alternar-se entre emissor e receptor, mas somente um por vez.

# BOA DIVERSÃO!
