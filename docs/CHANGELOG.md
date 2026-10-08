# HowTo SWT Pro Release Notes

## v1.2.0 — Offer Return & Context-aware Interaction

- 基座升级到 HowTo SWT Free v1.3.0，新增确定性的 `y = ax + b` 岗位收益函数、工时区间交点、最优区间与严格支配分析。
- 超过 3 个 Offer 时先显示全量列表，再选择最多 3 个做函数比较；宿主没有图形能力时完整退化为函数、表格、交点与区间结论。
- 新增共享 Interaction Capability Layer：已明确就执行，有限选择优先原生 UI，需要事实则输入；能力不可用时使用一致的编号／文本 fallback。
- Pro Context Builder 复用已确认的 Offer、工时偏好与阶段信息，避免重复询问，并支持 changed facts 后的确定性重算。
- 公开分发仍只包含加密 Bundle、SHA-256、manifest 与说明；Production Cloud 未在本次发布流程中修改。

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
