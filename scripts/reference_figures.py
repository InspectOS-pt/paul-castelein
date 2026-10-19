"""Paul's five original Meta reference posters, with accessible translations.

The WebP assets are byte-for-byte copies of the supplied reference. Their pixels
remain English; captions and full visual descriptions follow the page language.
The figures illustrate the thesis rather than report measured business results.

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
            "alt": "Replacing Trust with Proof: a comparison of unverified claims and verifiable evidence.",
            "caption": "Replacing trust with proof: from assumption to physical verification, ground-truth data and documented evidence.",
            "description": "The old model, shown in grey, lists information asymmetry, unverified claims, synthetic noise and paper documents marked with a cross. A blue arrow points to the new model: physical verification, ground-truth data and documented evidence, illustrated with a camera, measuring tool and checked shield. The footer describes the move from assumption to verification as measurable and auditable.",
        },
        2: {
            "alt": "The Business Model of 2030: verified reality and permissioned distribution.",
            "caption": "The Business Model of 2030: verified reality through InspectOS and RealOS, and permissioned distribution through Speaking Bricks and EstateOS.",
            "description": "A two-column conceptual model. Verified Reality, labelled InspectOS plus RealOS, shows building inspection, a thermal camera, a moisture meter, a paper-versus-reality check, a calculator and a checklist. Its foundations are physical verification, non-scrapable ground truth and regulatory compliance. Permissioned Distribution, labelled Speaking Bricks plus EstateOS, shows a network with permission gates, open/selected/closed disclosure tiers, CRM integration and anonymous buyer briefs. Its foundations are trust-gated protocols, authorized supply meeting represented demand, and filtering open-market noise.",
        },
        3: {
            "alt": "Information Asymmetry Collapse: from exclusive data access through abundant AI output to verified reality.",
            "caption": "Information asymmetry collapses as AI produces information at scale. The challenge shifts from finding information to verifying it.",
            "description": "Three stages run from left to right. Before: a locked case represents limited, secure, paywalled or monetized data. AI Explosion: a processor surrounded by documents and symbols represents synthetic creation, automated output and rapid replication. After: a funnel filters duplicate, fake and synthetic documents into a blue diamond labelled Verified Reality: curated, validated and trustworthy. The closing statement says the challenge is no longer finding information, but verifying it.",
        },
        4: {
            "alt": "The Vertical Data Flywheel: a circular connection between InspectOS, RealOS, Speaking Bricks and EstateOS.",
            "caption": "The Vertical Data Flywheel: InspectOS → RealOS → Speaking Bricks → EstateOS → back to InspectOS.",
            "description": "Four boxes sit around a circle connected by clockwise blue-purple arrows. InspectOS at the top is labelled Physical Verification. RealOS on the right is Buyer Intelligence. Speaking Bricks at the bottom is Permissioned Distribution. EstateOS on the left is Private Workspace. The circular arrangement illustrates the proposed relationship between physical evidence, buyer decisions, authorized professional distribution and private workspaces.",
        },
        5: {
            "alt": "The Five Moats of the Post-Software Era: five concentric layers surrounding a castle.",
            "caption": "Five layers for lasting value: ground-truth data, regulatory compliance, workflow depth, owned and permissioned distribution, and differentiation beyond commodity software.",
            "description": "Five concentric blue-grey rings surround a castle. The listed layers are: one, reliable and verified ground-truth data as the core foundation; two, regulatory compliance as a structural shield; three, process power and workflow depth; four, owned and permissioned distribution through direct channels and authorized access to customers; and five, avoiding the commodity software trap through differentiation beyond generic off-the-shelf software. The footer places layer one at the centre and describes additional outer layers as increasing defensibility. This is a conceptual strategy diagram.",
        },
    },
    "pt": {
        1: {
            "alt": "Substituir a confiança por provas: comparação entre afirmações não verificadas e evidências verificáveis.",
            "caption": "Substituir a confiança por provas: dos pressupostos à verificação física, aos dados reais verificados e à evidência documentada.",
            "description": "O modelo antigo, a cinzento, enumera assimetria de informação, afirmações não verificadas, ruído sintético e documentos em papel assinalados com uma cruz. Uma seta azul aponta para o novo modelo: verificação física, dados reais verificados e evidência documentada, ilustrados por uma câmara, um instrumento de medição e um escudo com um visto. O rodapé descreve a passagem dos pressupostos à verificação como mensurável e auditável.",
        },
        2: {
            "alt": "O Modelo de Negócio de 2030: realidade verificada e distribuição permissionada.",
            "caption": "O Modelo de Negócio de 2030: realidade verificada através da InspectOS e da RealOS, e distribuição permissionada através da Speaking Bricks e da EstateOS.",
            "description": "Modelo conceptual em duas colunas. Realidade Verificada, identificada como InspectOS mais RealOS, mostra uma inspeção de edifício, uma câmara térmica, um medidor de humidade, a comparação de documentos com a realidade, uma calculadora e uma lista de verificação. As suas bases são verificação física, dados reais não extraíveis por scraping e conformidade regulamentar. Distribuição Permissionada, identificada como Speaking Bricks mais EstateOS, mostra uma rede com controlo de permissões, três níveis de divulgação (aberto, selecionado e fechado), integração com CRM e resumos anónimos de compradores. As suas bases são protocolos de acesso controlado, oferta autorizada que encontra procura representada e filtragem do ruído do mercado aberto.",
        },
        3: {
            "alt": "Colapso da assimetria de informação: do acesso exclusivo aos dados à produção abundante por IA e à realidade verificada.",
            "caption": "A assimetria de informação diminui quando a IA produz informação em grande escala. O desafio passa de encontrar informação a verificá-la.",
            "description": "Três etapas, da esquerda para a direita. Antes: uma mala fechada à chave representa dados limitados, seguros e de acesso pago ou monetizado. Explosão da IA: um processador rodeado por documentos e símbolos representa criação sintética, produção automatizada e replicação rápida. Depois: um funil filtra documentos duplicados, falsos e sintéticos até obter um diamante azul, identificado como Realidade Verificada: selecionada, validada e fiável. A frase final diz que o desafio já não é encontrar informação, mas verificá-la.",
        },
        4: {
            "alt": "O ciclo de dados vertical: ligação circular entre InspectOS, RealOS, Speaking Bricks e EstateOS.",
            "caption": "O ciclo de dados vertical: InspectOS → RealOS → Speaking Bricks → EstateOS → de volta à InspectOS.",
            "description": "Quatro caixas estão dispostas num círculo e ligadas por setas azul-violeta no sentido dos ponteiros do relógio. A InspectOS, em cima, corresponde à Verificação Física. A RealOS, à direita, corresponde à Informação para Compradores. A Speaking Bricks, em baixo, corresponde à Distribuição Permissionada. A EstateOS, à esquerda, corresponde ao Espaço de Trabalho Privado. A disposição circular ilustra a relação proposta entre evidência física, decisões dos compradores, distribuição profissional autorizada e espaços privados de trabalho.",
        },
        5: {
            "alt": "As cinco defesas da era pós-software: cinco camadas concêntricas em torno de um castelo.",
            "caption": "Cinco camadas para criar valor duradouro: dados reais verificados, conformidade regulamentar, profundidade dos processos, distribuição própria e permissionada, e diferenciação para além do software comum.",
            "description": "Cinco anéis concêntricos azul-acinzentados rodeiam um castelo. As camadas enumeradas são: primeira, dados reais fiáveis e verificados como base central; segunda, conformidade regulamentar como proteção estrutural; terceira, capacidade dos processos e profundidade dos fluxos de trabalho; quarta, distribuição própria e permissionada através de canais diretos e de acesso autorizado aos clientes; quinta, evitar a dependência de software indiferenciado, criando diferenciação para além de soluções genéricas prontas a usar. O rodapé coloca a primeira camada no centro e descreve as camadas exteriores como reforços da capacidade de defesa. É um diagrama conceptual de estratégia.",
        },
    },
    "es": {
        1: {
            "alt": "Sustituir la confianza por pruebas: comparación entre afirmaciones sin verificar y evidencias verificables.",
            "caption": "Sustituir la confianza por pruebas: de las suposiciones a la verificación física, los datos verificados sobre el terreno y la evidencia documentada.",
            "description": "El modelo antiguo, en gris, enumera asimetría de información, afirmaciones sin verificar, ruido sintético y documentos en papel marcados con una cruz. Una flecha azul apunta al nuevo modelo: verificación física, datos verificados sobre el terreno y evidencia documentada, ilustrados con una cámara, una herramienta de medición y un escudo con una marca de verificación. El pie describe el paso de las suposiciones a la verificación como medible y auditable.",
        },
        2: {
            "alt": "El Modelo de Negocio de 2030: realidad verificada y distribución por permisos.",
            "caption": "El Modelo de Negocio de 2030: realidad verificada a través de InspectOS y RealOS, y distribución por permisos a través de Speaking Bricks y EstateOS.",
            "description": "Un modelo conceptual en dos columnas. Realidad Verificada, identificada como InspectOS más RealOS, muestra la inspección de un edificio, una cámara térmica, un medidor de humedad, la comparación entre documentos y realidad, una calculadora y una lista de comprobación. Sus bases son la verificación física, los datos reales no extraíbles mediante scraping y el cumplimiento normativo. Distribución por Permisos, identificada como Speaking Bricks más EstateOS, muestra una red con control de permisos, tres niveles de divulgación (abierto, seleccionado y cerrado), integración con CRM y resúmenes anónimos de compradores. Sus bases son los protocolos de acceso controlado, la oferta autorizada que encuentra demanda representada y el filtrado del ruido del mercado abierto.",
        },
        3: {
            "alt": "Colapso de la asimetría de información: del acceso exclusivo a los datos a la producción abundante de IA y a la realidad verificada.",
            "caption": "La asimetría de información disminuye cuando la IA produce información a gran escala. El desafío pasa de encontrar información a verificarla.",
            "description": "Tres etapas avanzan de izquierda a derecha. Antes: un maletín cerrado con llave representa datos limitados, seguros, de pago o monetizados. Explosión de IA: un procesador rodeado de documentos y símbolos representa creación sintética, producción automatizada y replicación rápida. Después: un embudo filtra documentos duplicados, falsos y sintéticos hasta obtener un diamante azul identificado como Realidad Verificada: seleccionada, validada y fiable. La frase final dice que el desafío ya no es encontrar información, sino verificarla.",
        },
        4: {
            "alt": "El ciclo de datos vertical: conexión circular entre InspectOS, RealOS, Speaking Bricks y EstateOS.",
            "caption": "El ciclo de datos vertical: InspectOS → RealOS → Speaking Bricks → EstateOS → de vuelta a InspectOS.",
            "description": "Cuatro recuadros se sitúan alrededor de un círculo y están unidos por flechas azul-violeta en el sentido de las agujas del reloj. InspectOS, arriba, corresponde a la Verificación Física. RealOS, a la derecha, corresponde a la Información para Compradores. Speaking Bricks, abajo, corresponde a la Distribución por Permisos. EstateOS, a la izquierda, corresponde al Espacio de Trabajo Privado. La disposición circular ilustra la relación propuesta entre evidencia física, decisiones de los compradores, distribución profesional autorizada y espacios privados de trabajo.",
        },
        5: {
            "alt": "Las cinco defensas de la era post-software: cinco capas concéntricas alrededor de un castillo.",
            "caption": "Cinco capas para crear valor duradero: datos verificados sobre el terreno, cumplimiento normativo, profundidad de los procesos, distribución propia y por permisos, y diferenciación más allá del software genérico.",
            "description": "Cinco anillos concéntricos azul-gris rodean un castillo. Las capas enumeradas son: primera, datos reales fiables y verificados como base central; segunda, cumplimiento normativo como protección estructural; tercera, capacidad de los procesos y profundidad de los flujos de trabajo; cuarta, distribución propia y por permisos mediante canales directos y acceso autorizado a los clientes; quinta, evitar la dependencia del software indiferenciado mediante una diferenciación que vaya más allá de las soluciones genéricas listas para usar. El pie sitúa la primera capa en el centro y describe las capas exteriores como refuerzos de la capacidad defensiva. Es un diagrama conceptual de estrategia.",
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
