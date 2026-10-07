# HowTo SWT Pro Release Notes

## v1.1.0 — Managed Lifecycle Context

### Milestone 1 — Orchestration base

- 基座升级到 HowTo SWT Free v1.2.0，采用 Router → Handoff → Executor → State Machine。

### Milestone 2 — Pro Lifecycle Context

- 增加 package 外的 Profile、SWT Case、Lifecycle、Domain Records 与 Event History。
- Context Builder 只加载当前任务所需上下文；Write Back 区分 confirmed、evidence 与 inference，并提供 VIEW、UPDATE、DELETE、EXPORT。

### Milestone 3 — Distribution Guard & Runtime Lifecycle

- 接入统一 Runtime Identity、Edition Guard、WorkBuddy flat-six adapter、24 小时 update check、atomic switch、verify 与 rollback。
- 更新资格到期不影响已安装版本继续使用；检查与应用严格分离。
- 公共发布物仍只有 encrypted bundle、manifest、README、release notes 与 public metadata。

### Offline Activation reliability

- 改进 Offline Activation 发布与密钥轮换机制。
- 提升多版本离线安装兼容性。
- 增强 Runtime 更新与恢复可靠性。

## v1.0.1 — Distribution Pilot

- 验证 public manifest、加密 bundle、ciphertext SHA-256、Offline Activation 与安全安装链路。
- 验证从 v1.0.0 到 v1.0.1 的更新流程。
- 本版本没有新增 SWT 业务能力；Production Cloud 尚未部署。

## v1.0.0 — Distribution MVP

- 建立以 HowTo SWT Free 为能力基座的 Pro overlay 发布流程。
- 增加授权安装、更新检查与私有分发所需的公开 metadata。
- 首版聚焦可靠安装与分发基础设施，不夸大 Pro 独有内容能力。
