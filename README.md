<h1 align="center">Gioia Zheng</h1>

<p align="center">
B.Sc. Student in Applied Computer Science and Artificial Intelligence<br>
Sapienza University of Rome, Italy
</p>

<p align="center">
<a href="https://gioiazheng.github.io">Website</a> ·
<a href="https://huggingface.co/GioiaZheng">Hugging Face</a> ·
<a href="https://www.linkedin.com/in/gioia-zheng-9233a0303">LinkedIn</a> ·
<a href="mailto:gioia.zheng.stud@gmail.com">Email</a> ·
<a href="cv/Gioia_Zheng_cv.pdf">Academic CV</a>
</p>

---

## About Me

I study information retrieval and retrieval-augmented generation, focusing on
when improvements in retrieval do—or do not—lead to more accurate and grounded
answers.

My work combines controlled retrieval and generation experiments with paired
evaluation, failure analysis, versioned manifests, and inspectable artifacts.

---

## Selected Work

| Project | Focus | Current scope |
| --- | --- | --- |
| [msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa) | Retrieval-augmented generation on MS MARCO | Retrieval, reranking, generation, grounding analysis, paired statistical evaluation, and reproducible experiment reports |
| [rag-observatory](https://github.com/GioiaZheng/rag-observatory) · [Live Space](https://huggingface.co/spaces/GioiaZheng/rag-observatory) | Trace-based analysis for RAG systems | Research prototype for inspecting retrieved evidence, generated answers, execution traces, and failure labels |
| [CiboCompass](https://github.com/GioiaZheng/CiboCompass) | Offline-resilient mobile food exploration | React Native, Go, and SQLite application with local caching, a persistent retry queue, and idempotent submission |

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
