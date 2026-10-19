"""Paul's latest editorial Meta illustrations, with accessible translations.

The WebP assets are byte-for-byte copies of the selected warm-paper originals
supplied on 19 October 2026. Their pixels remain English; captions and full visual
descriptions follow the page language. Source variation labels and the small
2024 footer are part of the original illustrations, not website publication dates.
These conceptual figures illustrate the thesis, not measured results or confirmed
operational capabilities.

API: reference_figure(number, lang, dark=False) -> HTML
"""

from html import escape


ASSETS = {
    1: ("replacing-trust-with-proof.webp", 880),
    2: ("business-model-2030.webp", 800),
    3: ("information-asymmetry-collapse.webp", 720),
    4: ("vertical-data-flywheel.webp", 820),
    5: ("five-moats.webp", 860),
}

COPY = {
    "en": {
        1: {
            "alt": "Replacing Trust with Proof: two columns compare assumptions and unverified claims with physical verification and documented evidence.",
            "caption": "A conceptual comparison: from assumptions and unverified claims to physical verification, ground-truth data and documented evidence.",
            "description": "A warm-paper illustration titled Replacing Trust with Proof, subtitled A founder's thesis: from assumption to verifiable evidence. A thin vertical line separates two columns, with a small arrow pointing right. The grey Trust column, labelled old workaround, shows a handshake for information asymmetry, a speech bubble for unverified claims and stacked sheets for synthetic noise. The black Proof column, labelled verified, shows a camera for physical verification, a measuring tool for ground-truth data, a checked shield for documented evidence and a grid for structured data. The small source footer reads From belief to evidence, 2024, Verify greater than believe.",
        },
        2: {
            "alt": "Business Model of 2030: two overlapping circles connect verified reality with permissioned distribution.",
            "caption": "A conceptual model for 2030: verified reality meets permissioned distribution.",
            "description": "Two thin black circles overlap on a warm-paper background. The left circle, Verified Reality, lists physical evidence, data described as non-scrapable and compliance. The right circle, Permissioned Distribution, lists trust-gated access, authorized supply plus represented demand and filtering automated noise. Their intersection is labelled Durable advantage over generalist software: the operating companies of 2030. The title and subtitle identify this as variation 3 of the Business Model of 2030 editorial diagram.",
        },
        3: {
            "alt": "Information Asymmetry Collapse: a vertical funnel moves from documents, claims and sources through verification to checked facts.",
            "caption": "A conceptual verification process: the challenge shifts from finding information to checking it.",
            "description": "The headline states that the primary challenge is no longer finding information, but verifying it. Below the Information Asymmetry Collapse, variation 3 label, a large outlined funnel contains layered sheets and the words Raw inputs: thousands of documents, claims, sources. An arrow leads down to a smaller funnel labelled Filter to verification and verification process. A second arrow leads to a black diamond with a check mark, labelled What can be physically and structurally verified. The closing line describes moving from volume to verified fact.",
        },
        4: {
            "alt": "The Vertical Data Flywheel: four ventures surround a circular loop for proprietary data within permitted boundaries.",
            "caption": "The data flywheel: InspectOS → RealOS → Speaking Bricks → EstateOS → back to InspectOS, within permitted boundaries.",
            "description": "Four outlined icon capsules sit around a large warm-stone circle, connected by thin black clockwise arrows. InspectOS at the top is labelled Physical verification. RealOS on the right is Buyer intelligence. Speaking Bricks at the bottom is Permissioned distribution. EstateOS on the left is Private workspace. The centre reads Compounding proprietary data within permitted boundaries.",
        },
        5: {
            "alt": "Five Moats: five nested rectangular frames place owned and permissioned distribution at the centre.",
            "caption": "A conceptual framework for lasting value: five nested frames, from avoiding commodity software to owned and permissioned distribution.",
            "description": "The title is Five Moats. A subtitle links durable advantage to the friction of the real world and owned channels. Five nested rectangular frames are numbered from the outside inward: I, Avoiding Commodity Software Trap; II, Ground Truth Data; III, Regulatory Compliance as Structural Shield; IV, Process Power and Workflow Depth; V, Owned and Permissioned Distribution. The innermost rectangle is black with white lettering; the outer frames use thin black lines, with small outline icons at the outer corners. It is a conceptual strategy diagram.",
        },
    },
    "pt": {
        1: {
            "alt": "Substituir a confiança por provas: duas colunas comparam pressupostos e afirmações não verificadas com a verificação física e a evidência documentada.",
            "caption": "Uma comparação conceptual: dos pressupostos e das afirmações não verificadas à verificação física, aos dados reais verificados e à evidência documentada.",
            "description": "Ilustração sobre papel de tom quente intitulada Substituir a Confiança por Provas, com o subtítulo A tese de um fundador: dos pressupostos à evidência verificável. Uma linha vertical fina separa duas colunas e uma pequena seta aponta para a direita. A coluna Confiança, a cinzento e identificada como solução anterior, mostra um aperto de mão para a assimetria de informação, um balão de fala para as afirmações não verificadas e folhas sobrepostas para o ruído sintético. A coluna Provas, a preto e identificada como verificada, mostra uma câmara para a verificação física, um instrumento de medição para os dados reais verificados, um escudo com um visto para a evidência documentada e uma grelha para os dados estruturados. O pequeno rodapé original diz Da crença à evidência, 2024, Verificar é preferível a acreditar.",
        },
        2: {
            "alt": "Modelo de Negócio de 2030: dois círculos sobrepostos ligam a realidade verificada à distribuição permissionada.",
            "caption": "Um modelo conceptual para 2030: a realidade verificada encontra a distribuição permissionada.",
            "description": "Dois círculos de traço preto fino sobrepõem-se sobre um fundo de papel de tom quente. O círculo da esquerda, Realidade Verificada, enumera evidência física, dados descritos como não extraíveis por scraping e conformidade regulamentar. O círculo da direita, Distribuição Permissionada, enumera acesso controlado pela confiança, oferta autorizada e procura representada, e filtragem do ruído automatizado. A interseção identifica uma Vantagem duradoura face ao software generalista: as empresas operacionais de 2030. O título e o subtítulo identificam a variação 3 do diagrama editorial Modelo de Negócio de 2030.",
        },
        3: {
            "alt": "Colapso da assimetria de informação: um funil vertical conduz documentos, afirmações e fontes através da verificação até aos factos verificados.",
            "caption": "Um processo conceptual de verificação: o desafio passa de encontrar informação a verificá-la.",
            "description": "O título afirma que o principal desafio já não é encontrar informação, mas verificá-la. Sob a indicação Colapso da Assimetria de Informação, variação 3, um grande funil desenhado a traço contém folhas sobrepostas e as palavras Dados de entrada: milhares de documentos, afirmações e fontes. Uma seta desce até um funil mais pequeno, identificado como Filtrar para verificar e processo de verificação. Uma segunda seta conduz a um losango preto com um visto, identificado como O que pode ser verificado física e estruturalmente. A frase final descreve a passagem do volume de informação ao facto verificado.",
        },
        4: {
            "alt": "O ciclo de dados vertical: quatro empresas rodeiam um ciclo de dados próprios dentro dos limites autorizados.",
            "caption": "O ciclo de dados: InspectOS → RealOS → Speaking Bricks → EstateOS → de volta à InspectOS, dentro dos limites autorizados.",
            "description": "Quatro cápsulas com ícones desenhados a traço rodeiam um grande círculo em tom de pedra quente e estão ligadas por setas pretas finas no sentido dos ponteiros do relógio. A InspectOS, em cima, corresponde à Verificação Física. A RealOS, à direita, corresponde à Informação para Compradores. A Speaking Bricks, em baixo, corresponde à Distribuição Permissionada. A EstateOS, à esquerda, corresponde ao Espaço de Trabalho Privado. No centro lê-se Acumulação de dados próprios dentro dos limites autorizados.",
        },
        5: {
            "alt": "Cinco defesas: cinco molduras retangulares encaixadas colocam a distribuição própria e permissionada no centro.",
            "caption": "Um enquadramento conceptual para criar valor duradouro: cinco molduras encaixadas, desde evitar o software indiferenciado até à distribuição própria e permissionada.",
            "description": "O título é Cinco Defesas. O subtítulo relaciona a vantagem duradoura com os obstáculos do mundo real e os canais próprios. Cinco molduras retangulares encaixadas são numeradas do exterior para o interior: I, Evitar a dependência de software indiferenciado; II, Dados reais verificados; III, Conformidade regulamentar como proteção estrutural; IV, Capacidade dos processos e profundidade dos fluxos de trabalho; V, Distribuição própria e permissionada. O retângulo central é preto, com letras brancas; as molduras exteriores usam linhas pretas finas e pequenos ícones de contorno nos cantos exteriores. É um diagrama conceptual de estratégia.",
        },
    },
    "es": {
        1: {
            "alt": "Sustituir la confianza por pruebas: dos columnas comparan suposiciones y afirmaciones sin verificar con la verificación física y la evidencia documentada.",
            "caption": "Una comparación conceptual: de las suposiciones y las afirmaciones sin verificar a la verificación física, los datos verificados sobre el terreno y la evidencia documentada.",
            "description": "Ilustración sobre papel de tono cálido titulada Sustituir la Confianza por Pruebas, con el subtítulo La tesis de un fundador: de las suposiciones a la evidencia verificable. Una fina línea vertical separa dos columnas y una pequeña flecha apunta hacia la derecha. La columna Confianza, en gris e identificada como solución anterior, muestra un apretón de manos para la asimetría de información, un bocadillo de diálogo para las afirmaciones sin verificar y hojas superpuestas para el ruido sintético. La columna Pruebas, en negro e identificada como verificada, muestra una cámara para la verificación física, una herramienta de medición para los datos verificados sobre el terreno, un escudo con una marca de verificación para la evidencia documentada y una cuadrícula para los datos estructurados. El pequeño pie original dice De la creencia a la evidencia, 2024, Verificar es preferible a creer.",
        },
        2: {
            "alt": "Modelo de Negocio de 2030: dos círculos superpuestos conectan la realidad verificada con la distribución por permisos.",
            "caption": "Un modelo conceptual para 2030: la realidad verificada se une a la distribución por permisos.",
            "description": "Dos círculos de trazo negro fino se superponen sobre un fondo de papel de tono cálido. El círculo izquierdo, Realidad Verificada, enumera evidencia física, datos descritos como no extraíbles mediante scraping y cumplimiento normativo. El círculo derecho, Distribución por Permisos, enumera acceso controlado por la confianza, oferta autorizada y demanda representada, y filtrado del ruido automatizado. La intersección se identifica como Ventaja duradera frente al software generalista: las empresas operativas de 2030. El título y el subtítulo identifican la variación 3 del diagrama editorial Modelo de Negocio de 2030.",
        },
        3: {
            "alt": "Colapso de la asimetría de información: un embudo vertical conduce documentos, afirmaciones y fuentes a través de la verificación hasta obtener hechos comprobados.",
            "caption": "Un proceso conceptual de verificación: el desafío pasa de encontrar información a comprobarla.",
            "description": "El titular afirma que el principal desafío ya no es encontrar información, sino verificarla. Bajo la indicación Colapso de la Asimetría de Información, variación 3, un gran embudo de contorno contiene hojas superpuestas y las palabras Datos de entrada: miles de documentos, afirmaciones y fuentes. Una flecha desciende hasta un embudo más pequeño, identificado como Filtrar para verificar y proceso de verificación. Una segunda flecha conduce a un rombo negro con una marca de verificación, identificado como Lo que puede verificarse física y estructuralmente. La frase final describe el paso del volumen de información al hecho verificado.",
        },
        4: {
            "alt": "El ciclo de datos vertical: cuatro empresas rodean un ciclo de datos propios dentro de los límites autorizados.",
            "caption": "El ciclo de datos: InspectOS → RealOS → Speaking Bricks → EstateOS → de vuelta a InspectOS, dentro de los límites autorizados.",
            "description": "Cuatro cápsulas con iconos de contorno rodean un gran círculo en tono piedra cálido y están conectadas mediante finas flechas negras en el sentido de las agujas del reloj. InspectOS, arriba, corresponde a la Verificación Física. RealOS, a la derecha, corresponde a la Información para Compradores. Speaking Bricks, abajo, corresponde a la Distribución por Permisos. EstateOS, a la izquierda, corresponde al Espacio de Trabajo Privado. El centro dice Acumulación de datos propios dentro de los límites autorizados.",
        },
        5: {
            "alt": "Cinco defensas: cinco marcos rectangulares anidados sitúan la distribución propia y por permisos en el centro.",
            "caption": "Un marco conceptual para crear valor duradero: cinco marcos anidados, desde evitar el software indiferenciado hasta la distribución propia y por permisos.",
            "description": "El título es Cinco Defensas. El subtítulo relaciona la ventaja duradera con las dificultades del mundo real y los canales propios. Cinco marcos rectangulares anidados se numeran de fuera hacia dentro: I, Evitar la dependencia del software indiferenciado; II, Datos verificados sobre el terreno; III, Cumplimiento normativo como protección estructural; IV, Capacidad de los procesos y profundidad de los flujos de trabajo; V, Distribución propia y por permisos. El rectángulo central es negro, con letras blancas; los marcos exteriores usan finas líneas negras y pequeños iconos de contorno en las esquinas exteriores. Es un diagrama conceptual de estrategia.",
        },
    },
}


def reference_figure(n, lang, dark=False):
    """Render one original poster with a localized caption and long description.

    ``dark`` changes the outer caption styling hook, never the original image.
    The caller supplies CSS for the reference-figure classes and ``sr-only``.
    """
    filename, max_width = ASSETS[n]
    copy = COPY[lang][n]
    description_id = f"reference-figure-{n}-{lang}-description"
    classes = "reference-figure" + (" reference-figure--dark" if dark else "")
    note = {
        "en": "",
        "pt": "Imagem original em inglês.",
        "es": "Imagen original en inglés.",
    }[lang]
    translated_note = (
        f' <span class="reference-figure__language">{escape(note)}</span>'
        if note else ""
    )
    return (
        f'<figure class="{classes}" style="--figure-max:{max_width}px">'
        '<div class="reference-figure__frame">'
        f'<img src="/assets/infographics/{filename}" width="1920" height="1280" '
        f'alt="{escape(copy["alt"], quote=True)}" aria-describedby="{description_id}" '
        'loading="lazy" decoding="async">'
        '</div>'
        '<figcaption class="reference-figure__caption">'
        f'<span class="reference-figure__number">Fig. {n}</span>'
        f'<span class="reference-figure__text">{escape(copy["caption"])}{translated_note}</span>'
        '</figcaption>'
        f'<div id="{description_id}" class="reference-figure__description sr-only">'
        f'{escape(copy["description"])}'
        '</div>'
        '</figure>'
    )
