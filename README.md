<h1 align="center">Gioia Zheng</h1>

<p align="center">
B.Sc. Student in Applied Computer Science and Artificial Intelligence<br>
Sapienza University of Rome, Italy
</p>

<p align="center">
<a href="https://gioiazheng.github.io">Website</a> ·
<a href="https://www.linkedin.com/in/gioia-zheng-9233a0303">LinkedIn</a> ·
<a href="mailto:gioia.zheng.stud@gmail.com">Email</a> ·
<a href="cv/Gioia_Zheng_cv.pdf">Academic CV</a>
</p>

---

## About Me

I study information retrieval and retrieval-augmented generation, focusing on
when improvements in retrieval do—or do not—lead to more accurate and grounded
answers.

My work examines how retrieval, reranking, evidence use, and generation errors
interact; how evaluation choices affect experimental conclusions; and how
failure analysis can reveal regressions hidden by aggregate metrics.

I build reproducible ML research pipelines using controlled baselines, paired
comparisons, confidence intervals, versioned experiment manifests, and
inspectable artifacts.

---

## Selected Work

| Project | Focus | Highlights |
| --- | --- | --- |
| [msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa) | Retrieval-augmented generation on MS MARCO | Reproducible retrieval, reranking, generation, grounding analysis, paired statistical evaluation, CI, and experiment reports |
| [rag-observatory](https://github.com/GioiaZheng/rag-observatory) | Trace-based observability for RAG systems | Local-first tooling for inspecting retrieved evidence, generated answers, execution traces, and failure categories |
| [CiboCompass](https://github.com/GioiaZheng/CiboCompass) | Offline-first mobile food exploration | React Native, Go, and SQLite application focused on synchronization, practical UX, and cultural menu understanding |
| [go-chat-system](https://github.com/GioiaZheng/go-chat-system) | Full-stack chat application | Go REST APIs, Vue frontend, SQLite persistence, authentication, OpenAPI documentation, testing, and CI |

---

## Current Research

**Research question:** When does better retrieval improve grounded generation,
and when do conventional evaluation metrics hide the failure?

**Current study:** Controlled retrieve–rerank–generate experiments on MS MARCO,
using paired statistical evaluation, explicit grounding measures, and
per-example failure analysis.

**Research direction:** Developing a versioned RAG failure taxonomy that
distinguishes retrieval, reranking, evidence-use, and generation errors.

---

## Open Source Contributions

I contribute targeted fixes, tests, documentation, and evaluation improvements
to open-source retrieval and machine-learning tools.

### Merged Upstream

- [MTEB #4861](https://github.com/embeddings-benchmark/mteb/pull/4861) —
  documented the model-evaluation request workflow.
- [MTEB Leaderboard #31](https://github.com/embeddings-benchmark/leaderboard-frontend/pull/31) —
  added model language-scope metadata, tests, and accessibility coverage.

### Active Contributions

- [BEIR #218](https://github.com/beir-cellar/beir/pull/218) and
  [BEIR #219](https://github.com/beir-cellar/beir/pull/219) —
  regression fixes for dense exact search and Hugging Face Dataset inputs.
- [LangChain LiteLLM #212](https://github.com/langchain-ai/langchain-litellm/pull/212) —
  support for the `base_url` embeddings configuration path.
- [RAGChecker #39](https://github.com/amazon-science/RAGChecker/pull/39) —
  clarified metric input requirements and the boundaries of reference-free
  evaluation.

---

## Technical Profile

**Research areas:** Information retrieval, retrieval-augmented generation,
grounding evaluation, failure analysis

**Evaluation methods:** Paired bootstrap, confidence intervals, controlled
ablations, Token-F1, ROUGE-L, BLEU, exact match

**Models and tools:** Python, PyTorch, BM25, FAISS, Sentence-BERT,
cross-encoder reranking, T5

**Research infrastructure:** Linux, Docker, Git, GitHub Actions, experiment
manifests, reproducible pipelines

**Languages:** Chinese — Native · Italian — Bilingual · English — Professional ·
German — Beginner
