<h1 align="center">Gioia Zheng</h1>

<p align="center">
B.Sc. in Applied Computer Science & Artificial Intelligence<br>
Sapienza University of Rome · Italy
</p>

<p align="center">
<a href="mailto:gioia.zheng.stud@gmail.com">Email</a> ·
<a href="https://www.linkedin.com/in/gioia-zheng-9233a0303">LinkedIn</a> ·
<a href="cv/Zheng_Gioia_cv.pdf">Resume</a> ·
<a href="https://github.com/GioiaZheng">GitHub</a>
</p>

---

## Overview

Undergraduate at Sapienza University of Rome, working at the intersection of **information retrieval**, **retrieval-augmented generation**, and **reproducible ML evaluation**.

*Open to research collaborations and full-time roles in Search / IR, ML systems, or backend (Italy / EU / remote).*

---

## Recent Work

**NLP Algorithm Engineer Intern — Microsoft, Natural Language Computing (Remote)** *(Feb – May 2026)*

End-to-end RAG pipeline on MS MARCO with a statistical-evaluation framework:

- Cross-encoder reranking of dense top-100 **doubled generation Token-F1 (0.197 → 0.368)** on full dev/small (6,980 queries); 95% paired-bootstrap CIs on all four metric Δs strictly above 0.
- DistilBERT BERTScore proxy on 3,000 paired examples confirmed the gain is **not** a surface-form artefact (Δ +0.173).
- Deterministic regression-failure taxonomy: **~90% of regressions are generator-side truncation**, not retrieval or semantic failure.
- Surfaced an **NLI-entailment Δ sign reversal (−0.145)** — the only metric in the pipeline whose paired Δ reverses sign — motivating a generator-capacity follow-up rather than a decode-budget fix.
- 286 unit tests, per-run provenance manifest, lockfile, CI on every push.

Public deliverable: [`msmarco-genqa`](https://github.com/GioiaZheng/msmarco-genqa).

---

## Selected Projects

### [msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa) — Information Retrieval / RAG
**Python · PyTorch · BM25 · FAISS · Cross-encoder · T5**

Reproducible single-machine RAG pipeline on MS MARCO with a paired-bootstrap evaluation framework and a regression-failure taxonomy. Headline numbers under *Recent Work* above.

### [handwritten-ocr-system](https://github.com/GioiaZheng/handwritten-ocr-system) — Computer Vision / Sequence Modeling
**PyTorch · CNN + BiLSTM + CTC**

End-to-end OCR pipeline trained on the IAM handwriting dataset; CER / WER evaluation on held-out splits.

### [go-chat-system](https://github.com/GioiaZheng/go-chat-system) — Backend Engineering
**Go · Vue · SQLite · OpenAPI**

Concurrent Go backend with REST API and embedded Vue frontend; documented under OpenAPI.

### [CiboCompass](https://github.com/GioiaZheng/CiboCompass) — Mobile / Full-stack
**React Native · Go · SQLite**

Cross-platform mobile app with offline-first sync for international students reading Italian restaurant menus.

---

## Technical Skills

- **Programming** — Python · Go · JavaScript · SQL
- **ML & Retrieval** — PyTorch · BM25 · FAISS · dense retrieval · cross-encoder reranking · RAG · paired-bootstrap CI · BERTScore · NLI grounding
- **Backend & Systems** — REST APIs · concurrent backend (Go) · Docker · Linux · Git · GitHub Actions CI

---

## Languages

English (Professional) · Italian (Bilingual) · Chinese (Native) · German (Beginner)
