<h1 align="center">Gioia Zheng</h1>

<p align="center">
B.Sc. Student in Applied Computer Science and Artificial Intelligence<br>
Sapienza University of Rome, Italy
</p>

<p align="center">
<a href="https://gioiazheng.github.io">Website</a> ·
<a href="https://huggingface.co/GioiaZheng">Hugging Face</a> ·
<a href="https://www.linkedin.com/in/gioiazheng/">LinkedIn</a> ·
<a href="mailto:gioia.zheng.stud@gmail.com">Email</a> ·
<a href="cv/Gioia_Zheng_cv.pdf">Academic CV</a>
</p>

---

## About Me

Research focus: Information Retrieval, RAG/LLM Evaluation, Reproducible ML
Systems, and Reinforcement Learning for game and embodied agents.

I study information retrieval and retrieval-augmented generation, focusing on
when improvements in retrieval do—or do not—lead to more accurate and grounded
answers.

My work combines controlled retrieval and generation experiments with paired
evaluation, observability, failure analysis, versioned manifests, and
inspectable artifacts.

---

## Selected Work

| Project | Focus | Current scope |
| --- | --- | --- |
| [rag-observatory](https://github.com/GioiaZheng/rag-observatory) · [Live Space](https://huggingface.co/spaces/GioiaZheng/rag-observatory) · [Toy Dataset](https://huggingface.co/datasets/GioiaZheng/rag-observatory-toy-traces) | Trace-based analysis for RAG systems | Research prototype for inspecting retrieved evidence, generated answers, execution traces, and failure labels |
| [msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa) · [Benchmark Runs](https://huggingface.co/datasets/GioiaZheng/msmarco-genqa-benchmark-runs) | Retrieval-augmented generation on MS MARCO | Retrieval, reranking, generation, grounding analysis, paired statistical evaluation, and reproducible experiment reports |
| [q-learning-exploitability](https://github.com/GioiaZheng/q-learning-exploitability) · [Evidence Map](https://gioiazheng.github.io/projects/q-learning-exploitability/) | Exact agent evaluation and controlled failure analysis | Adversarial backups and D4 evidence pooling reduced force-loss policies from 6/6 to 0/6 under matched Q-update budgets |
| [Public research artifacts](https://huggingface.co/GioiaZheng) | Reusable evidence for evaluation work | Hugging Face datasets / Spaces, versioned reports, release archives, manifests, and trace examples connected back to the source repositories |

---

## Selected Open-Source Contributions

Only merged, publicly verifiable contributions are listed here.

| Ecosystem | Contribution | Evidence |
| --- | --- | --- |
| MTEB | Fixed duplicate counting for symmetric STS pairs. | [embeddings-benchmark/mteb#4958](https://github.com/embeddings-benchmark/mteb/pull/4958) |
| Pyserini | Fixed M-BEIR instruction lookup from cache-home paths. | [castorini/pyserini#2655](https://github.com/castorini/pyserini/pull/2655) |
| MTEB | Updated GermanGovService retrieval to the v2 dataset. | [embeddings-benchmark/mteb#5323](https://github.com/embeddings-benchmark/mteb/pull/5323) |
| MTEB Leaderboard | Added model language-scope display on leaderboard cards. | [embeddings-benchmark/leaderboard-frontend#31](https://github.com/embeddings-benchmark/leaderboard-frontend/pull/31) |

---

## Current Research

**Research question:** When does better retrieval improve grounded generation,
and when do conventional evaluation metrics hide the failure?

**Current study:** Controlled retrieve–rerank–generate experiments on MS MARCO,
using paired statistical evaluation, explicit grounding measures, and
per-example failure analysis.

**Research direction:** Developing a versioned RAG failure taxonomy that
distinguishes retrieval, reranking, evidence-use, and generation errors.
