# HowTo SWT Pro

## 01 Hero

HowTo SWT Pro 是管理完整 SWT 生命周期的会员版：在 Free 的完整单任务能力上增加 persistent profile、过程状态、历史记录、Context Builder 与受控 Write Back。

**HowTo SWT Pro v1.2.0** · Created by Howard

本仓库只承载 public manifest、encrypted bundle、公开说明和必要 metadata；不包含 Pro 明文源码、会员数据、Secret 或私钥。

## 02 Agent 安装

Pro 通过公开 [HowTo SWT CLI](https://github.com/0x-howard/howto-swt-cli) 授权安装与更新。Online 服务目前仍是显式 Pilot / staging，不冒充 Production；受限网络 Agent 使用 device-bound Offline Activation。

| Agent | 当前验证状态 |
|---|---|
| Codex | ✅ package Runtime、完整业务回归与当前会话 capability inventory 已验收；无 picker 时使用文本 fallback |
| WorkBuddy | ◐ flat-six 安装与 lifecycle 已集成测试，并核对本机 Runtime 的 structured-choice 静态证据；未做真实 UI E2E |
| 豆包 Work | ◐ Offline Activation、interaction contract 与文本 fallback 回归通过；未验证正式 choice/form UI |
| Claude Code | ◐ package adapter、interaction contract 与文本 fallback 回归通过；未做真实宿主 UI 验收 |

[查看安装与授权边界 →](docs/INSTALL.md)

## 03 Free vs Pro

| 产品 | 正式边界 |
|---|---|
| Free | 在当前会话内完成一个完整 SWT 任务 |
| Pro | 跨会话管理一个完整 SWT 过程 |
| SWT 陪跑营 | Pro + 社群 + 直播 + 真人判断／复核／陪跑 |

OTP、Offline Activation 与 encrypted bundle 是 entitlement infrastructure，不是 Pro 的主要用户价值。

## 04 核心能力

- 继承 Free v1.3.0 的 Router、Handoff、五个 Domain Executor、Offer Return Function 与 Interaction Capability Layer。
- Canonical Profile、SWT Case、Lifecycle、Offer、English、Visa、housing、documents metadata 与 Event History。
- Context Builder 按当前 Executor / intent 只加载相关信息。
- Confirmed / Evidence / Inference 分级 Write Back；Inference 必须先确认。
- VIEW、UPDATE、DELETE、EXPORT，以及新会话恢复。
- Runtime Identity、Edition Guard、24h update check、atomic switch、verify 与 rollback。

## 05 使用方式

```text
你好小How
小How帮我看看这个岗位
陪我练 Sponsor 面试
小How，你现在记得我什么？
把我的 Sponsor 改成 CIEE。
删除之前那个 Offer。
导出我的 SWT 档案。
```

更新检查不会抢占任务。会员更新资格到期后，已安装 Pro 仍可继续使用；若有新版，只说明更新资格已到期，不提供可执行更新提示。

## 06 数据与隐私

- Persistent Context 只允许位于 package 外、由宿主显式指定的 `USER_DATA_ROOT`。
- Pro package、Git、overlay、references 与本 Dist 仓库不保存用户长期数据。
- Evidence Fact 保存 source/document reference 与 confidence；Inference 未经确认不得持久化。
- 会员邮箱只用于 entitlement；OTP、session token、activation token、release key 和私钥不进入本仓库。

## 07 最近 5 个版本

<!-- CHANGELOG_LATEST_START -->
| 版本 | 更新 |
|---|---|
| v1.2.0 | 新增岗位收益函数、工时区间最优分析与 context-aware 跨 Agent 交互。 |
| v1.1.0 | 增加 Managed Lifecycle Context，并接入统一 Task/Runtime 架构与受控更新生命周期。 |
| v1.0.1 | 验证加密发布、Offline Activation 与安全更新链路；无新增业务能力。 |
| v1.0.0 | 建立基于 Free 的 Pro overlay 与授权分发基础。 |
<!-- CHANGELOG_LATEST_END -->

[查看完整更新日志 →](docs/CHANGELOG.md)

## 08 Author

HowTo SWT  
作者：Howard  
@哎哟不想上早八啊（全平台同名） · GitHub：[`0x-howard`](https://github.com/0x-howard)
