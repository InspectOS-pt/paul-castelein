"""Paul's latest Swiss Bold / terracotta Meta originals, accessibly translated.

The WebP assets are byte-for-byte copies of the five personal-site illustrations
supplied on 19 October 2026. Their pixels remain English; captions and full visual
descriptions follow the page language. Each asset retains its original aspect
ratio, including the portrait Five Moats poster.

API: reference_figure(number, lang, dark=False) -> HTML
"""

from html import escape


ASSETS = {
    1: ("replacing-trust-with-proof.webp", 880, 1920, 1280),
    2: ("business-model-2030.webp", 800, 1920, 1280),
    3: ("information-asymmetry-collapse.webp", 720, 1920, 1280),
    4: ("vertical-data-flywheel.webp", 820, 1920, 1280),
    5: ("five-moats.webp", 680, 1344, 1792),
}

COPY = {
    "en": {
        1: {
            "alt": "Replacing Trust with Proof: a terracotta arrow connects trust issues with standards of verifiable evidence.",
            "caption": "Replacing trust with proof: physical verification, ground-truth data and documented evidence.",
            "description": "Two heavy black frames sit beneath the title Replacing Trust with Proof. The stone-coloured Trust panel lists information asymmetry, unverified claims and no audit trail, illustrated by a handshake, speech bubble and question-mark document. Its footer reads Subjective, reliant on relationship, no audit trail. A large terracotta arrow points to the Proof panel, which lists physical verification, ground truth and documented evidence beside a camera, measuring tool and checked shield. Its footer reads Objective, measured, repeatable, traceable. The closing line describes a shift from reliance to verifiable facts, designed for clarity, accountability and transparency.",
        },
        2: {
            "alt": "The Business Model of 2030: verified reality through InspectOS and RealOS alongside permissioned distribution through Speaking Bricks and EstateOS.",
            "caption": "The Business Model of 2030: verified reality and permissioned distribution.",
            "description": "A two-column poster with heavy black frames and terracotta accents. The Verified Reality column, labelled InspectOS plus RealOS, shows building inspection, a thermal camera, a moisture meter, paper versus reality, a calculator and a checklist. Three bullets identify physical verification, non-scrapable ground truth and regulatory compliance. The Permissioned Distribution column, labelled Speaking Bricks plus EstateOS, shows a network gate; three black bars marked Open, Selected and Closed; a CRM icon; and an anonymous brief. The footer reads Data-led, privacy-preserving, built for 2030, and Verified, permissioned, scalable.",
        },
        3: {
            "alt": "Information Asymmetry Collapse: three panels move from restricted access, through an AI flood of information, to verification.",
            "caption": "The challenge is no longer finding information, but verifying physical facts, authority and genuine intent.",
            "description": "Three black-framed panels appear beneath the title Information Asymmetry Collapse. Before shows a locked stone doorway and document stacks, labelled Exclusive access monetized: limited, restricted, costly. AI Era shows large AI lettering surrounded by flying documents, labelled Flood of information: overload, unverified, noise. Now shows documents entering a funnel and emerging as a terracotta diamond with a white check mark. Its highlighted text reads Verifying physical facts, authority, genuine intent, followed by Synthesized, verified, trusted. The closing statement says the challenge is no longer finding information, but verifying it.",
        },
        4: {
            "alt": "The Vertical Data Flywheel: InspectOS, RealOS, Speaking Bricks and EstateOS surround a terracotta cycle of compounding proprietary data.",
            "caption": "The data flywheel: InspectOS → RealOS → Speaking Bricks → EstateOS → back to InspectOS, within permitted boundaries.",
            "description": "Four heavy black frames surround a clockwise loop of terracotta arrows. InspectOS, at upper left, is labelled Physical verification and illustrated by an inspection icon. RealOS, at upper right, is labelled Buyer intelligence with an ascending chart. Speaking Bricks, at lower right, is labelled Permissioned distribution network with a network gate. EstateOS, at lower left, is labelled Private workspace with a padlock. The terracotta centre reads Compounding proprietary data. The footer describes data being collected, validated, activated, protected and reinvested to compound advantage. The accompanying caption retains the requirement that data use stays within permitted boundaries.",
        },
        5: {
            "alt": "The Five Moats of the Post-Software Era: five stacked panels outline sources of durable business advantage.",
            "caption": "Five sources of lasting value: differentiation, ground-truth data, compliance, workflow depth and permissioned distribution.",
            "description": "A portrait poster has a black title band and five stacked, black-bordered panels with terracotta numbered icons. I: Avoiding Commodity Software Trap, differentiate via domain expertise. II: Ground Truth Data, own proprietary real-world data. III: Regulatory Compliance as Structural Shield, embed compliance into structure. IV: Process Power and Workflow Depth, deep integrated workflows. V: Owned and Permissioned Distribution, direct owned channels. White and warm-stone panels alternate. The black footer states that when software becomes abundant, code alone ceases to be a lasting advantage.",
        },
    },
    "pt": {
        1: {
            "alt": "Substituir a confiança por provas: uma seta em terracota liga os problemas da confiança aos critérios de evidência verificável.",
            "caption": "Substituir a confiança por provas: verificação física, dados reais verificados e evidência documentada.",
            "description": "Duas molduras pretas espessas surgem sob o título Substituir a Confiança por Provas. O painel Confiança, em tom de pedra, enumera assimetria de informação, afirmações não verificadas e ausência de rasto de auditoria, ilustradas por um aperto de mão, um balão de fala e um documento com um ponto de interrogação. O seu rodapé diz Subjetivo, dependente de relações, sem rasto de auditoria. Uma grande seta em terracota aponta para o painel Provas, que enumera verificação física, dados reais verificados e evidência documentada junto de uma câmara, um instrumento de medição e um escudo com um visto. O seu rodapé diz Objetivo, medido, repetível, rastreável. A frase final descreve a passagem da confiança aos factos verificáveis, com clareza, responsabilização e transparência.",
        },
        2: {
            "alt": "O Modelo de Negócio de 2030: realidade verificada através da InspectOS e da RealOS, ao lado da distribuição permissionada através da Speaking Bricks e da EstateOS.",
            "caption": "O Modelo de Negócio de 2030: realidade verificada e distribuição permissionada.",
            "description": "Cartaz em duas colunas com molduras pretas espessas e apontamentos em terracota. A coluna Realidade Verificada, identificada como InspectOS mais RealOS, mostra uma inspeção de edifício, uma câmara térmica, um medidor de humidade, a comparação de documentos com a realidade, uma calculadora e uma lista de verificação. Três pontos identificam verificação física, dados reais não extraíveis por scraping e conformidade regulamentar. A coluna Distribuição Permissionada, identificada como Speaking Bricks mais EstateOS, mostra uma rede com controlo de acesso; três barras pretas com as indicações Aberto, Selecionado e Fechado; um ícone de CRM; e um resumo anónimo. O rodapé diz Baseado em dados, com proteção da privacidade, concebido para 2030, e Verificado, permissionado, escalável.",
        },
        3: {
            "alt": "Colapso da assimetria de informação: três painéis passam do acesso restrito à abundância de informação da IA e à verificação.",
            "caption": "O desafio já não é encontrar informação, mas verificar factos físicos, autoridade e intenção genuína.",
            "description": "Três painéis com molduras pretas surgem sob o título Colapso da Assimetria de Informação. Antes mostra uma porta de pedra fechada e pilhas de documentos, com a indicação Acesso exclusivo monetizado: limitado, restrito, dispendioso. Era da IA mostra as letras IA rodeadas por documentos em movimento, com a indicação Abundância de informação: sobrecarga, informação não verificada, ruído. Agora mostra documentos a entrar num funil e a sair como um losango em terracota com um visto branco. O texto em destaque diz Verificar factos físicos, autoridade, intenção genuína, seguido de Sintetizado, verificado, fiável. A frase final diz que o desafio já não é encontrar informação, mas verificá-la.",
        },
        4: {
            "alt": "O ciclo de dados vertical: InspectOS, RealOS, Speaking Bricks e EstateOS rodeiam um ciclo em terracota de acumulação de dados próprios.",
            "caption": "O ciclo de dados: InspectOS → RealOS → Speaking Bricks → EstateOS → de volta à InspectOS, dentro dos limites autorizados.",
            "description": "Quatro molduras pretas espessas rodeiam um ciclo de setas em terracota no sentido dos ponteiros do relógio. A InspectOS, em cima à esquerda, corresponde à Verificação Física e apresenta um ícone de inspeção. A RealOS, em cima à direita, corresponde à Informação para Compradores e apresenta um gráfico ascendente. A Speaking Bricks, em baixo à direita, corresponde à Rede de Distribuição Permissionada e apresenta uma rede com controlo de acesso. A EstateOS, em baixo à esquerda, corresponde ao Espaço de Trabalho Privado e apresenta um cadeado. No centro, em terracota, lê-se Acumulação de dados próprios. O rodapé descreve a recolha, validação, ativação, proteção e reinvestimento de dados para reforçar a vantagem. A legenda mantém o requisito de utilização dos dados dentro dos limites autorizados.",
        },
        5: {
            "alt": "As Cinco Defesas da Era Pós-Software: cinco painéis sobrepostos apresentam fontes de vantagem empresarial duradoura.",
            "caption": "Cinco fontes de valor duradouro: diferenciação, dados reais verificados, conformidade, profundidade dos processos e distribuição permissionada.",
            "description": "Cartaz vertical com uma faixa preta de título e cinco painéis empilhados, de contorno preto e com ícones numerados em terracota. I: Evitar a Dependência de Software Indiferenciado, diferenciar através do conhecimento especializado do setor. II: Dados Reais Verificados, possuir dados próprios do mundo real. III: Conformidade Regulamentar como Proteção Estrutural, integrar a conformidade na estrutura. IV: Capacidade dos Processos e Profundidade dos Fluxos de Trabalho, fluxos de trabalho profundamente integrados. V: Distribuição Própria e Permissionada, canais próprios diretos. Os painéis alternam entre branco e tom de pedra quente. O rodapé preto afirma que, quando o software se torna abundante, o código por si só deixa de constituir uma vantagem duradoura.",
        },
    },
    "es": {
        1: {
            "alt": "Sustituir la confianza por pruebas: una flecha terracota conecta los problemas de la confianza con criterios de evidencia verificable.",
            "caption": "Sustituir la confianza por pruebas: verificación física, datos verificados sobre el terreno y evidencia documentada.",
            "description": "Dos marcos negros gruesos aparecen bajo el título Sustituir la Confianza por Pruebas. El panel Confianza, en tono piedra, enumera asimetría de información, afirmaciones sin verificar y ausencia de registro de auditoría, ilustradas mediante un apretón de manos, un bocadillo de diálogo y un documento con un signo de interrogación. Su pie dice Subjetivo, dependiente de las relaciones, sin registro de auditoría. Una gran flecha terracota apunta al panel Pruebas, que enumera verificación física, datos verificados sobre el terreno y evidencia documentada junto a una cámara, una herramienta de medición y un escudo con una marca de verificación. Su pie dice Objetivo, medido, repetible, trazable. La frase final describe el paso de la confianza a los hechos verificables, con claridad, responsabilidad y transparencia.",
        },
        2: {
            "alt": "El Modelo de Negocio de 2030: realidad verificada mediante InspectOS y RealOS junto a distribución por permisos mediante Speaking Bricks y EstateOS.",
            "caption": "El Modelo de Negocio de 2030: realidad verificada y distribución por permisos.",
            "description": "Cartel de dos columnas con marcos negros gruesos y detalles terracota. La columna Realidad Verificada, identificada como InspectOS más RealOS, muestra una inspección de edificios, una cámara térmica, un medidor de humedad, la comparación de documentos con la realidad, una calculadora y una lista de comprobación. Tres puntos identifican verificación física, datos reales no extraíbles mediante scraping y cumplimiento normativo. La columna Distribución por Permisos, identificada como Speaking Bricks más EstateOS, muestra una red con control de acceso; tres barras negras marcadas Abierto, Seleccionado y Cerrado; un icono de CRM; y un informe anónimo. El pie dice Basado en datos, con protección de la privacidad, diseñado para 2030, y Verificado, con permisos, escalable.",
        },
        3: {
            "alt": "Colapso de la asimetría de información: tres paneles pasan del acceso restringido a la abundancia de información de la IA y a la verificación.",
            "caption": "El desafío ya no es encontrar información, sino verificar hechos físicos, autoridad e intención genuina.",
            "description": "Tres paneles con marcos negros aparecen bajo el título Colapso de la Asimetría de Información. Antes muestra una puerta de piedra cerrada y pilas de documentos, con la indicación Acceso exclusivo monetizado: limitado, restringido, costoso. Era de la IA muestra las letras IA rodeadas de documentos en movimiento, con la indicación Abundancia de información: sobrecarga, información sin verificar, ruido. Ahora muestra documentos entrando en un embudo y saliendo como un rombo terracota con una marca de verificación blanca. El texto destacado dice Verificar hechos físicos, autoridad, intención genuina, seguido de Sintetizado, verificado, fiable. La frase final dice que el desafío ya no es encontrar información, sino verificarla.",
        },
        4: {
            "alt": "El ciclo de datos vertical: InspectOS, RealOS, Speaking Bricks y EstateOS rodean un ciclo terracota de acumulación de datos propios.",
            "caption": "El ciclo de datos: InspectOS → RealOS → Speaking Bricks → EstateOS → de vuelta a InspectOS, dentro de los límites autorizados.",
            "description": "Cuatro marcos negros gruesos rodean un ciclo de flechas terracota en el sentido de las agujas del reloj. InspectOS, arriba a la izquierda, corresponde a la Verificación Física y muestra un icono de inspección. RealOS, arriba a la derecha, corresponde a la Información para Compradores y muestra un gráfico ascendente. Speaking Bricks, abajo a la derecha, corresponde a la Red de Distribución por Permisos y muestra una red con control de acceso. EstateOS, abajo a la izquierda, corresponde al Espacio de Trabajo Privado y muestra un candado. El centro terracota dice Acumulación de datos propios. El pie describe la recopilación, validación, activación, protección y reinversión de datos para reforzar la ventaja. La leyenda mantiene el requisito de utilizar los datos dentro de los límites autorizados.",
        },
        5: {
            "alt": "Las Cinco Defensas de la Era Post-Software: cinco paneles apilados presentan fuentes de ventaja empresarial duradera.",
            "caption": "Cinco fuentes de valor duradero: diferenciación, datos verificados sobre el terreno, cumplimiento normativo, profundidad de los procesos y distribución por permisos.",
            "description": "Cartel vertical con una banda negra de título y cinco paneles apilados, de contorno negro y con iconos numerados en terracota. I: Evitar la Dependencia del Software Indiferenciado, diferenciarse mediante el conocimiento especializado del sector. II: Datos Verificados sobre el Terreno, poseer datos propios del mundo real. III: Cumplimiento Normativo como Protección Estructural, integrar el cumplimiento en la estructura. IV: Capacidad de los Procesos y Profundidad de los Flujos de Trabajo, flujos de trabajo profundamente integrados. V: Distribución Propia y por Permisos, canales propios directos. Los paneles alternan entre blanco y tono piedra cálido. El pie negro afirma que, cuando el software se vuelve abundante, el código por sí solo deja de constituir una ventaja duradera.",
        },
    },
}


def reference_figure(n, lang, dark=False):
    """Render one original poster with a localized caption and long description.

    ``dark`` changes the outer caption styling hook, never the original image.
    The caller supplies CSS for the reference-figure classes and ``sr-only``.
    """
    filename, max_width, width, height = ASSETS[n]
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
        f'<img src="/assets/infographics/{filename}" width="{width}" height="{height}" '
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
