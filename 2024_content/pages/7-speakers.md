Title: Keynotes
Date: 2024-07-26

<hr>

<div class="container">
<div class="row display-flex">

    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4">
    <div class="thumbnail">
        <a href="#mohit">
        <img
            src="{static}/images/speakers_200x200/mohit_iyyer.jpg"
            alt="Mohit Iyyer"
            style="width:88%"
            align="center">
        <div class="caption">
            <h5>Mohit Iyyer</h5>
            <p>University of Massachusetts Amherst, Associate Professor
            </p>
            <p></p>
        </div>
        </a>
    </div>
    </div>


    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4">
    <div class="thumbnail">
        <a href="#patrick">
        <img
            src="{static}/images/speakers_200x200/patrick_lewis.jpg"
            alt="Patrick Lewis"
            style="width:88%"
            align="center">
        <div class="caption">
            <h5>Patrick Lewis</h5>
            <p>Cohere, Research Scientist
            </p>
            <p></p>
        </div>
        </a>
    </div>
    </div>

    <!-- 6/12 = 1/2 width on mobile, 4/12 = 1/3 screen on laptop -->
    <div class="col-xs-6 col-md-4">
    <div class="thumbnail">
        <a href="#juan">
        <img
            src="{static}/images/speakers_200x200/juan_sequeda.jpg"
            alt="Juan Sequeda"
            style="width:88%"
            align="center">
        <div class="caption">
            <h5>Juan Sequeda</h5>
            <p>data.world, Principal Scientist
            </p>
            <p></p>
        </div>
        </a>
    </div>
    </div>


</div>
</div>
<br />


# Talks

### <a id="mohit"></a> Mohit Iyyer: How can retrieval aid long-form text generation?

Large language models (LLMs) encode huge amounts of knowledge about the world into their parameters. However, this parametric knowledge is often insufficient to generate accurate and specific information about arbitrary user-selected topics. The emerging area of retrieval-augmented language models thus aims to give LLMs access to external data, but how well do these methods improve long-form text generation (i.e., where the output can be very long)? In this talk, I first provide an overview of the modeling and evaluation challenges associated with retrieval-augmented long-form question answering. Next, I show that methods such as the kNN-LM may not actually improve the generation quality of language models, again highlighting the challenge of evaluation for future research. Finally, I propose a high-level framework (applicable to both human and LLM-based evaluation) that first decomposes a long-form text into simpler atomic units before then evaluating each unit on a specific aspect via retrieval. I demonstrate the framework's effectiveness at evaluating factuality and faithfulness on tasks such as book summarization and biography generation. However, this framework's limitations begin to show as tasks and contexts become increasingly complex, as I show with a case study of claim verification on long novels, where all tested models perform far worse than humans.

### <a id="patrick"></a> Patrick Lewis: RAG, Past, Present, Future

In this talk I’ll reflect on progress made on Retrieval-augmentation since the publication of 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks’, a paper from 2020 that introduced the ’RAG’ acronym to the world and helped to popularise RAG techniques. We’ll examine what remains the same, what has changed, and where I think we should focus our energy next.


### <a id="juan"></a> Juan Sequeda: Increasing the LLM Accuracy for Question Answering on Structured Data: Knowledge Graphs to the Rescue!

Our research aims to understand the accuracy of LLM-powered question answering systems in the context of enterprise questions, SQL databases, and knowledge graphs. We introduce a benchmark comprising an enterprise SQL schema in the insurance domain, a range of enterprise queries encompassing reporting to metrics, and a contextual layer incorporating an ontology and mappings that define a knowledge graph. Our first finding reveals that question answering using GPT-4, with zero-shot prompts directly on SQL databases, achieves an accuracy of 16%. Notably, this accuracy increases to 54% when questions are posed over a Knowledge Graph representation of the enterprise SQL database, thus a 3X increase in accuracy.

The question remains: how can we further improve the accuracy? Building on the observations of our first work where the inaccurate LLM-generated SPARQL queries followed incorrect paths, we present a Ontology-based Query Check (OBQC) approach which 1) leverages the ontology of the knowledge graph to check if the LLM-generated SPARQL query matches the semantic of ontology to detect errors and 2) use the explanations of the errors with an LLM to repair the errors. Our next finding is that this approach increases the overall accuracy to 72% including an additional 8% of unknown results. The overall error rate of 20%. Thus an overall 4X accuracy improvement.

Our call to action is to invest in Knowledge Graph to provide higher accuracy for LLM powered question answering systems over structured data.
