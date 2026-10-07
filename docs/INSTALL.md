# HowTo SWT Pro 安装说明

HowTo SWT Pro 只通过公开 [HowTo SWT CLI](https://github.com/0x-howard/howto-swt-cli) 安装。本仓库不提供明文 Pro package。

## Online Pilot

当前 Online endpoint 仍需显式配置 Pilot / staging 地址；Production Cloud 本轮未修改。CLI 先做 Edition detection，再发起 entitlement 与 OTP 流程。不同 Edition 会返回 `EDITION_REPLACE_CONFIRMATION_REQUIRED`，用户再次明确确认后才能 APPLY。

## Offline Activation

受限网络 Agent 先在本机生成 device-bound Activation Request，再在用户自己的浏览器完成 OTP，最后将 Activation Token 带回原设备。CLI 会验签并核对 product、version、request 与 device binding，再下载本仓库的 encrypted bundle、校验 ciphertext SHA-256、解密并复用同一原子 installer。

## 数据与更新

安装目标的 Runtime Identity 与 persistent SWT context 分离。更新不会触碰 `USER_DATA_ROOT`。会员更新资格到期后已安装版本继续可用，但不能激活新版本。
