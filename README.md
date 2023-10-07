# WORD_BOT
※このプログラムは現在開発中であり、初期段階のためコードが不十分です。また、BOTの公開予定はありません。

**Introduction**\n
このプログラムはReplitで作成されたDiscordBOT開発用のプログラムです。\n
チャットコマンドにより禁止ワードを設定し自動削除を行う、また制限されているワードをユーザーの権限ごとに管理することを目的としています。\n
\n
**Feature**\n
主な機能は前述した通り\n
`!add_word [1]    //ワードをリストに追加\n
 !remove_word [1] //ワードをリストから削除\n
 Auther.OpenList  //ワードリストをチャットに公開`\n
上記のコマンドをDiscordのチャット内に打つことでBOTがそれぞれの命令に対応した行動をとります。\n
もし会話内容に禁止ワードが含まれている場合は\n
`f'{message.author.mention} 禁止ワードが含まれています!')`\n
と返します。\n
\n
**Development environments**\n
Replit(python3-)\n
https://replit.com/~\n
UptimeRobot\n
https://uptimerobot.com/\n
